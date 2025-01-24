# based on https://github.com/isl-org/MiDaS

import os

import cv2
import torch
import torch.nn as nn
from torchvision.transforms import Compose

from .midas.dpt_depth import DPTDepthModel
from .midas.midas_net import MidasNet
from .midas.midas_net_custom import MidasNet_small
from .midas.transforms import NormalizeImage, PrepareForNet, Resize


def disabled_train(self, mode=True):
    """Overwrite model.train with this function to make sure train/eval mode
    does not change anymore."""
    return self


def load_midas_transform(model_type):
    # https://github.com/isl-org/MiDaS/blob/master/run.py
    # load transform only
    if model_type == 'dpt_large':  # DPT-Large
        net_w, net_h = 384, 384
        resize_mode = 'minimal'
        normalization = NormalizeImage(
            mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])

    elif model_type == 'dpt_hybrid':  # DPT-Hybrid
        net_w, net_h = 384, 384
        resize_mode = 'minimal'
        normalization = NormalizeImage(
            mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])

    elif model_type == 'midas_v21':
        net_w, net_h = 384, 384
        resize_mode = 'upper_bound'
        normalization = NormalizeImage(
            mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])

    elif model_type == 'midas_v21_small':
        net_w, net_h = 256, 256
        resize_mode = 'upper_bound'
        normalization = NormalizeImage(
            mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])

    else:
        assert False, f"model_type '{model_type}' not implemented, use: --model_type large"

    transform = Compose([
        Resize(
            net_w,
            net_h,
            resize_target=None,
            keep_aspect_ratio=True,
            ensure_multiple_of=32,
            resize_method=resize_mode,
            image_interpolation_method=cv2.INTER_CUBIC,
        ),
        normalization,
        PrepareForNet(),
    ])

    return transform


def load_model(model_type, model_root_path):
    # https://github.com/isl-org/MiDaS/blob/master/run.py
    # load network
    ISL_PATHS = {
        'dpt_large': os.path.join(model_root_path,
                                  'dpt_large-midas-2f21e586.pt'),
        'dpt_hybrid': os.path.join(model_root_path,
                                   'dpt_hybrid-midas-501f0c75.pt'),
        'midas_v21': '',
        'midas_v21_small': '',
    }
    model_path = ISL_PATHS[model_type]
    if model_type == 'dpt_large':  # DPT-Large
        model = DPTDepthModel(
            path=model_path,
            backbone='vitl16_384',
            non_negative=True,
        )
        net_w, net_h = 384, 384
        resize_mode = 'minimal'
        normalization = NormalizeImage(
            mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])

    elif model_type == 'dpt_hybrid':  # DPT-Hybrid
        model = DPTDepthModel(
            path=model_path,
            backbone='vitb_rn50_384',
            non_negative=True,
        )
        net_w, net_h = 384, 384
        resize_mode = 'minimal'
        normalization = NormalizeImage(
            mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])

    elif model_type == 'midas_v21':
        model = MidasNet(model_path, non_negative=True)
        net_w, net_h = 384, 384
        resize_mode = 'upper_bound'
        normalization = NormalizeImage(
            mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])

    elif model_type == 'midas_v21_small':
        model = MidasNet_small(
            model_path,
            features=64,
            backbone='efficientnet_lite3',
            exportable=True,
            non_negative=True,
            blocks={'expand': True})
        net_w, net_h = 256, 256
        resize_mode = 'upper_bound'
        normalization = NormalizeImage(
            mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])

    else:
        print(
            f"model_type '{model_type}' not implemented, use: --model_type large"
        )
        assert False

    transform = Compose([
        Resize(
            net_w,
            net_h,
            resize_target=None,
            keep_aspect_ratio=True,
            ensure_multiple_of=32,
            resize_method=resize_mode,
            image_interpolation_method=cv2.INTER_CUBIC,
        ),
        normalization,
        PrepareForNet(),
    ])

    return model.eval(), transform


class MiDaSInference(nn.Module):
    MODEL_TYPES_TORCH_HUB = ['DPT_Large', 'DPT_Hybrid', 'MiDaS_small']
    MODEL_TYPES_ISL = [
        'dpt_large',
        'dpt_hybrid',
        'midas_v21',
        'midas_v21_small',
    ]

    def __init__(self, model_type, model_root_path):
        super().__init__()
        assert (model_type in self.MODEL_TYPES_ISL)
        model, _ = load_model(model_type, model_root_path)
        self.model = model
        self.model.train = disabled_train

    def forward(self, x):
        with torch.no_grad():
            prediction = self.model(x)
        return prediction
