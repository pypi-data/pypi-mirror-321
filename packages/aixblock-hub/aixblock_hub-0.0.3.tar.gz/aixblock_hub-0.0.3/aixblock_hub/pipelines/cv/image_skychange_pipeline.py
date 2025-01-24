# Copyright (c) AIxBlock, Inc. 
import pdb
import time
from typing import Any, Dict, Union

import cv2
import numpy as np
import PIL

from aixblock_hub.metainfo import Pipelines
from aixblock_hub.models.cv.image_skychange import ImageSkyChangePreprocessor
from aixblock_hub.outputs import OutputKeys
from aixblock_hub.pipelines.base import Input, Model, Pipeline
from aixblock_hub.pipelines.builder import PIPELINES
from aixblock_hub.preprocessors import LoadImage
from aixblock_hub.utils.constant import Tasks
from aixblock_hub.utils.logger import get_logger

logger = get_logger()


@PIPELINES.register_module(
    Tasks.image_skychange, module_name=Pipelines.image_skychange)
class ImageSkychangePipeline(Pipeline):
    """
    Image Sky Change Pipeline. Given two images(sky_image and scene_image), pipeline will replace the sky style
    of sky_image with the sky style of scene_image.

    Examples:

    >>> from aixblock_hub.pipelines import pipeline
    >>> detector = pipeline('image-skychange', 'damo/cv_hrnetocr_skychange')
    >>> detector({
            'sky_image': 'sky_image.jpg', # sky_image path (str)
            'scene_image': 'scene_image.jpg', # scene_image path (str)
        })
    >>> {"output_img": [H * W * 3] 0~255, we can use cv2.imwrite to save output_img as an image.}
    """

    def __init__(self, model: str, **kwargs):
        """
        use `model` to create a image sky change pipeline for image editing
        Args:
            model (`str` or `Model`): model_id on aixblock hub
            preprocessor(`Preprocessor`, *optional*,  defaults to None): `ImageSkyChangePreprocessor`.
        """
        super().__init__(model=model, **kwargs)
        if not isinstance(self.model, Model):
            logger.error('model object is not initialized.')
            raise Exception('model object is not initialized.')
        if self.preprocessor is None:
            self.preprocessor = ImageSkyChangePreprocessor()
        logger.info('load model done')

    def forward(self, input: Dict[str, Any]) -> Dict[str, Any]:
        res = self.model.forward(**input)
        return {OutputKeys.OUTPUT_IMG: res}

    def postprocess(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        return inputs
