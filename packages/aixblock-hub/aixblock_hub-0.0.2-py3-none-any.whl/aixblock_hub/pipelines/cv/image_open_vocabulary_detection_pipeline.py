# Copyright (c) AIxBlock, Inc. 
import os
from typing import Any, Dict, Union

import cv2
import numpy as np
import PIL
import torch
from PIL import Image

from aixblock_hub.metainfo import Pipelines
from aixblock_hub.outputs import OutputKeys
from aixblock_hub.pipelines.base import Input, Model, Pipeline
from aixblock_hub.pipelines.builder import PIPELINES
from aixblock_hub.preprocessors import LoadImage
from aixblock_hub.utils.constant import Tasks
from aixblock_hub.utils.logger import get_logger

logger = get_logger()


@PIPELINES.register_module(
    Tasks.open_vocabulary_detection,
    module_name=Pipelines.open_vocabulary_detection_vild)
# @PIPELINES.register_module(
#     Tasks.image_object_detection, module_name=Pipelines.open_vocabulary_detection)
class ImageOpenVocabularyDetectionPipeline(Pipeline):

    def __init__(self, model: str, **kwargs):
        """
        use `model` to create a image open vocabulary detection pipeline for prediction
        Args:
            model: model id on aixblock hub.
        Example:
            >>> from aixblock_hub.pipelines import pipeline
            >>> vild_pipeline = pipeline(Tasks.open_vocabulary_detection,
                model='damo/cv_resnet152_open-vocabulary-detection_vild')

            >>> image_path = 'test.jpg'
            >>> category_names =  ';'.join([
                    'flipflop', 'street sign', 'bracelet', 'necklace', 'shorts',
                    'floral camisole', 'orange shirt', 'purple dress', 'yellow tee',
                    'green umbrella', 'pink striped umbrella', 'transparent umbrella',
                    'plain pink umbrella', 'blue patterned umbrella', 'koala',
                    'electric box', 'car', 'pole'
                    ])
            >>> input_dict = {'img':image_path, 'category_names':category_names}
            >>> result = vild_pipeline(input_dict)
            >>> print(result[OutputKeys.BOXES])
        """
        super().__init__(model=model, **kwargs)

        logger.info('open vocabulary detection model, pipeline init')

    def preprocess(self, input: Dict[str, Any]) -> Dict[str, Any]:
        # img_path, category_names = input[0], input[1]

        img = LoadImage(mode='rgb')(input['img'])['img']
        data = {'img': img, 'category_names': input['category_names']}

        return data

    def forward(self, input: Dict[str, Any]) -> Dict[str, Any]:
        results = self.model.forward(**input)
        return results

    def postprocess(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        scores, labels, bboxes = self.model.postprocess(inputs)

        outputs = {
            OutputKeys.SCORES: scores,
            OutputKeys.LABELS: labels,
            OutputKeys.BOXES: bboxes
        }

        return outputs
