# Copyright (c) AIxBlock, Inc. 

from typing import Any, Dict

import torch
import torchvision.transforms as T

from aixblock_hub.metainfo import Pipelines
from aixblock_hub.outputs import OutputKeys
from aixblock_hub.pipelines.base import Input, Pipeline
from aixblock_hub.pipelines.builder import PIPELINES
from aixblock_hub.preprocessors import LoadImage
from aixblock_hub.utils.constant import Tasks
from aixblock_hub.utils.logger import get_logger

logger = get_logger()


@PIPELINES.register_module(
    Tasks.semantic_segmentation,
    module_name=Pipelines.ddpm_image_semantic_segmentation)
class DDPMImageSemanticSegmentationPipeline(Pipeline):

    def __init__(self, model: str, **kwargs):
        """use `model` to create a image semantic segmentation pipeline for prediction

        Args:
            model: model id on aixblock hub
        """
        _device = kwargs.pop('device', 'gpu')
        if torch.cuda.is_available() and _device == 'gpu':
            self.device = 'gpu'
        else:
            self.device = 'cpu'
        super().__init__(model=model, device=self.device, **kwargs)

        logger.info('Load model done!')

    def preprocess(self, input: Input) -> Dict[str, Any]:
        image = LoadImage.convert_to_img(input)
        assert image.size[0] == image.size[1], \
            f'Only square images are supported: ({image.size[0]}, {image.size[1]})'

        infer_transforms = T.Compose(
            [T.Resize(256), T.ToTensor(), lambda x: 2 * x - 1])
        image = infer_transforms(image)

        result = {'input_img': image}

        return result

    def forward(self, input: Dict[str, Any],
                **forward_params) -> Dict[str, Any]:
        with torch.no_grad():
            output = self.model(input)
        return output

    def postprocess(self, inputs, **kwargs) -> Dict[str, Any]:
        mask, out_img = inputs
        return {OutputKeys.MASKS: mask[0], OutputKeys.OUTPUT_IMG: out_img[0]}
