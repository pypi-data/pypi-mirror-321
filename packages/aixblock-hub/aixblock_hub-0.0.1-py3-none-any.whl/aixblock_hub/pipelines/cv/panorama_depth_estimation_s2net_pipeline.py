# Copyright (c) AIxBlock, Inc. 
from typing import Any, Dict, Union

import cv2
import numpy as np
import PIL
import torch

from aixblock_hub.metainfo import Pipelines
from aixblock_hub.outputs import OutputKeys
from aixblock_hub.pipelines.base import Input, Model, Pipeline
from aixblock_hub.pipelines.builder import PIPELINES
from aixblock_hub.preprocessors import LoadImage
from aixblock_hub.utils.constant import Tasks
from aixblock_hub.utils.cv.image_utils import depth_to_color
from aixblock_hub.utils.logger import get_logger

logger = get_logger()


@PIPELINES.register_module(
    Tasks.panorama_depth_estimation,
    module_name=Pipelines.panorama_depth_estimation_s2net)
class PanoramaDepthEstimationPipeline(Pipeline):
    """ This pipeline will estimation the depth panoramic image from one rgb panoramic image.
        The input panoramic image should be equirectanlar, in the size of 512x1024.

    Examples:

    >>> import cv2
    >>> from aixblock_hub.outputs import OutputKeys
    >>> from aixblock_hub.pipelines import pipeline
    >>> from aixblock_hub.utils.constant import Tasks

    >>> task = 'panorama-depth-estimation'
    >>> model_id = 'damo/cv_s2net_image-depth-estimation'

    >>> input_location = 'data/test/images/panorama_depth_estimation.jpg'
    >>> estimator = pipeline(Tasks.panorama_depth_estimation, model=model_id)
    >>> result = estimator(input_location)
    >>> depth_vis = result[OutputKeys.DEPTHS_COLOR]
    >>> cv2.imwrite('result.jpg', depth_vis)
    """

    def __init__(self, model: str, **kwargs):
        """
        use `model` to create a panorama depth estimation pipeline for prediction
        Args:
            model: model id on aixblock hub.
        """
        super().__init__(model=model, **kwargs)

        logger.info('depth estimation model, pipeline init')

    def preprocess(self, input: Input) -> Dict[str, Any]:
        img = LoadImage.convert_to_ndarray(input)
        H, W = 512, 1024
        img = cv2.resize(img, dsize=(W, H), interpolation=cv2.INTER_CUBIC)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        rgb = self.model.to_tensor(img.copy())
        rgb = self.model.normalize(rgb)[None, ...]
        return rgb

    def forward(self, input: Dict[str, Any]) -> Dict[str, Any]:
        results = self.model.forward(input)
        return results

    def postprocess(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        results = self.model.postprocess(inputs)
        depths = results[OutputKeys.DEPTHS]
        if isinstance(depths, torch.Tensor):
            depths = depths.detach().cpu().squeeze().numpy()
        depths_color = depth_to_color(depths)
        outputs = {
            OutputKeys.DEPTHS: depths,
            OutputKeys.DEPTHS_COLOR: depths_color
        }
        return outputs
