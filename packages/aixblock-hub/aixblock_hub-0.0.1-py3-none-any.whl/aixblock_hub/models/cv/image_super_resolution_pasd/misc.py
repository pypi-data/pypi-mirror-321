# Part of the implementation is borrowed and modified from StableSR,
# publicly available at https://github.com/IceClear/StableSR/blob/main/scripts/wavelet_color_fix.py
import torch
from diffusers.pipelines.stable_diffusion.convert_from_ckpt import (
    convert_ldm_unet_checkpoint, convert_ldm_vae_checkpoint)
from PIL import Image
from safetensors import safe_open
from torch import Tensor
from torch.nn import functional as F
from torchvision.transforms import ToPILImage, ToTensor


def adain_color_fix(target: Image, source: Image):
    # Convert images to tensors
    to_tensor = ToTensor()
    target_tensor = to_tensor(target).unsqueeze(0)
    source_tensor = to_tensor(source).unsqueeze(0)

    # Apply adaptive instance normalization
    result_tensor = adaptive_instance_normalization(target_tensor,
                                                    source_tensor)

    # Convert tensor back to image
    to_image = ToPILImage()
    result_image = to_image(result_tensor.squeeze(0).clamp_(0.0, 1.0))

    return result_image


def wavelet_color_fix(target: Image, source: Image):
    # Convert images to tensors
    to_tensor = ToTensor()
    target_tensor = to_tensor(target).unsqueeze(0)
    source_tensor = to_tensor(source).unsqueeze(0)

    # Apply wavelet reconstruction
    result_tensor = wavelet_reconstruction(target_tensor, source_tensor)

    # Convert tensor back to image
    to_image = ToPILImage()
    result_image = to_image(result_tensor.squeeze(0).clamp_(0.0, 1.0))

    return result_image


def calc_mean_std(feat: Tensor, eps=1e-5):
    """Calculate mean and std for adaptive_instance_normalization.
    Args:
        feat (Tensor): 4D tensor.
        eps (float): A small value added to the variance to avoid
            divide-by-zero. Default: 1e-5.
    """
    size = feat.size()
    assert len(size) == 4, 'The input feature should be 4D tensor.'
    b, c = size[:2]
    feat_var = feat.reshape(b, c, -1).var(dim=2) + eps
    feat_std = feat_var.sqrt().reshape(b, c, 1, 1)
    feat_mean = feat.reshape(b, c, -1).mean(dim=2).reshape(b, c, 1, 1)
    return feat_mean, feat_std


def adaptive_instance_normalization(content_feat: Tensor, style_feat: Tensor):
    """Adaptive instance normalization.
    Adjust the reference features to have the similar color and illuminations
    as those in the degradate features.
    Args:
        content_feat (Tensor): The reference feature.
        style_feat (Tensor): The degradate features.
    """
    size = content_feat.size()
    style_mean, style_std = calc_mean_std(style_feat)
    content_mean, content_std = calc_mean_std(content_feat)
    normalized_feat = (content_feat
                       - content_mean.expand(size)) / content_std.expand(size)
    return normalized_feat * style_std.expand(size) + style_mean.expand(size)


def wavelet_blur(image: Tensor, radius: int):
    """
    Apply wavelet blur to the input tensor.
    """
    # input shape: (1, 3, H, W)
    # convolution kernel
    kernel_vals = [
        [0.0625, 0.125, 0.0625],
        [0.125, 0.25, 0.125],
        [0.0625, 0.125, 0.0625],
    ]
    kernel = torch.tensor(kernel_vals, dtype=image.dtype, device=image.device)
    # add channel dimensions to the kernel to make it a 4D tensor
    kernel = kernel[None, None]
    # repeat the kernel across all input channels
    kernel = kernel.repeat(3, 1, 1, 1)
    image = F.pad(image, (radius, radius, radius, radius), mode='replicate')
    # apply convolution
    output = F.conv2d(image, kernel, groups=3, dilation=radius)
    return output


def wavelet_decomposition(image: Tensor, levels=5):
    """
    Apply wavelet decomposition to the input tensor.
    This function only returns the low frequency & the high frequency.
    """
    high_freq = torch.zeros_like(image)
    for i in range(levels):
        radius = 2**i
        low_freq = wavelet_blur(image, radius)
        high_freq += (image - low_freq)
        image = low_freq

    return high_freq, low_freq


def wavelet_reconstruction(content_feat: Tensor, style_feat: Tensor):
    """
    Apply wavelet decomposition, so that the content will have the same color as the style.
    """
    # calculate the wavelet decomposition of the content feature
    content_high_freq, content_low_freq = wavelet_decomposition(content_feat)
    del content_low_freq
    # calculate the wavelet decomposition of the style feature
    style_high_freq, style_low_freq = wavelet_decomposition(style_feat)
    del style_high_freq
    # reconstruct the content feature with the style's high frequency
    return content_high_freq + style_low_freq


def load_dreambooth_lora(unet, vae=None, model_path=None, model_base=''):
    if model_path is None:
        return unet

    if model_path.endswith('.ckpt'):
        base_state_dict = torch.load(model_path)['state_dict']
    elif model_path.endswith('.safetensors'):
        state_dict = {}
        with safe_open(model_path, framework='pt', device='cpu') as f:
            for key in f.keys():
                state_dict[key] = f.get_tensor(key)

        is_lora = all('lora' in k for k in state_dict.keys())
        if not is_lora:
            base_state_dict = state_dict
        else:
            base_state_dict = {}
            with safe_open(model_base, framework='pt', device='cpu') as f:
                for key in f.keys():
                    base_state_dict[key] = f.get_tensor(key)

    converted_unet_checkpoint = convert_ldm_unet_checkpoint(
        base_state_dict, unet.config)
    unet.load_state_dict(converted_unet_checkpoint, strict=False)

    if vae is not None:
        converted_vae_checkpoint = convert_ldm_vae_checkpoint(
            base_state_dict, vae.config)
        vae.load_state_dict(converted_vae_checkpoint)

    return unet, vae
