# Copyright (c) AIxBlock, Inc. 
import os.path as osp
from typing import Any, Dict

import cv2
import numpy as np
import PIL
import torch
import torch.nn.functional as F
from torch import nn
from torchvision import transforms

from aixblock_hub.metainfo import Pipelines
from aixblock_hub.outputs import OutputKeys
from aixblock_hub.pipelines import pipeline
from aixblock_hub.pipelines.base import Input, Pipeline
from aixblock_hub.pipelines.builder import PIPELINES
from aixblock_hub.preprocessors import LoadImage
from aixblock_hub.utils.constant import ModelFile, Tasks
from aixblock_hub.utils.logger import get_logger

logger = get_logger()


@PIPELINES.register_module(
    Tasks.image_classification, module_name=Pipelines.content_check)
class ContentCheckPipeline(Pipeline):

    def __init__(self, model: str, **kwargs):
        """
        use `model` to create a content check pipeline for prediction
        Args:
            model: model id on aixblock hub.
        Example:
        ContentCheckPipeline can judge whether the picture is pornographic

        ```python
        >>> from aixblock_hub.pipelines import pipeline
        >>> cc_func = pipeline('image_classification', 'damo/cv_resnet50_image-classification_cc')
        >>> cc_func("https://app.aixblock.io/test/images/content_check.jpg")
        {'scores': [0.2789826989173889], 'labels': 'pornographic'}
        ```
        """

        # content check model
        super().__init__(model=model, **kwargs)
        self.test_transforms = transforms.Compose([
            transforms.Resize(224),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])
        logger.info('content check model loaded!')

    def preprocess(self, input: Input) -> Dict[str, Any]:
        img = LoadImage.convert_to_img(input)
        img = self.test_transforms(img).float()
        result = {}
        result['img'] = img
        return result

    def forward(self, input: Dict[str, Any]) -> Dict[str, Any]:
        img = input['img'].unsqueeze(0)
        result = self.model(img)
        score = [1 - F.softmax(result[:, :5])[0][-1].tolist()]
        if score[0] < 0.5:
            label = 'pornographic'
        else:
            label = 'normal'
        return {OutputKeys.SCORES: score, OutputKeys.LABELS: label}

    def postprocess(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        return inputs
