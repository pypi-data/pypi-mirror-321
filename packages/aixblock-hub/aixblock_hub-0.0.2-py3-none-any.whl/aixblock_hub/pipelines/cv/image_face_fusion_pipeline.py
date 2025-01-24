# Copyright (c) AIxBlock, Inc. 
from typing import Any, Dict

import numpy as np

from aixblock_hub.metainfo import Pipelines
from aixblock_hub.outputs import OutputKeys
from aixblock_hub.pipelines.base import Input, Pipeline
from aixblock_hub.pipelines.builder import PIPELINES
from aixblock_hub.preprocessors import LoadImage
from aixblock_hub.utils.constant import ModelFile, Tasks
from aixblock_hub.utils.logger import get_logger

logger = get_logger()


@PIPELINES.register_module(
    Tasks.image_face_fusion, module_name=Pipelines.image_face_fusion)
class ImageFaceFusionPipeline(Pipeline):
    """
    Image face fusion pipeline.

    Examples:

    >>> from aixblock_hub.pipelines import pipeline
    >>> image_face_fusion = pipeline(Tasks.image_face_fusion,
                   model='damo/cv_unet-image-face-fusion_damo')
    >>> image_face_fusion({
            'template': 'facefusion_template.jpg', # template path (str)
            'image': 'facefusion_user.jpg', # user path (str)
        })
       {
        "output_img": [H * W * 3] 0~255, we can use cv2.imwrite to save output_img as an image.
        }
    """

    def __init__(self, model: str, **kwargs):
        """
        use `model` to create image-face-fusion pipeline for prediction
        Args:
            model: model id on aixblock hub.
        """
        super().__init__(model=model, **kwargs)
        logger.info('image face fusion model init done')

    def preprocess(self,
                   template: Input,
                   user: Input = None) -> Dict[str, Any]:
        if type(template) is dict:  # for demo service
            user = template['user']
            template = template['template']

        template_img = LoadImage.convert_to_ndarray(template)
        user_img = LoadImage.convert_to_ndarray(user)

        result = {'template': template_img, 'user': user_img}
        return result

    def forward(self, input: Dict[str, Any]) -> Dict[str, Any]:
        template_img = input['template']
        user_img = input['user']
        output = self.model.inference(template_img, user_img)
        result = {'outputs': output}
        return result

    def postprocess(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        output_img = inputs['outputs']
        return {OutputKeys.OUTPUT_IMG: output_img}
