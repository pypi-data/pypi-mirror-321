# Copyright 2021-2022 The Alibaba Fundamental Vision  Team Authors. All rights reserved.

import math
import os.path as osp
from typing import Any, Dict

import numpy as np
import torch
import torchvision.transforms as transforms
from mmcv.parallel import collate, scatter

from aixblock_hub.metainfo import Pipelines
from aixblock_hub.models.cv.vision_middleware import VisionMiddlewareModel
from aixblock_hub.outputs import OutputKeys
from aixblock_hub.pipelines.base import Input, Pipeline
from aixblock_hub.pipelines.builder import PIPELINES
from aixblock_hub.preprocessors import LoadImage
from aixblock_hub.utils.config import Config
from aixblock_hub.utils.constant import ModelFile, Tasks
from aixblock_hub.utils.logger import get_logger

logger = get_logger()


@PIPELINES.register_module(
    Tasks.image_segmentation,
    module_name=Pipelines.vision_middleware_multi_task)
class VisionMiddlewarePipeline(Pipeline):

    def __init__(self, model: str, **kwargs):
        """
        use `model` to create a vision middleware pipeline for prediction
        Args:
            model: model id on aixblock hub.
        """
        super().__init__(model=model, **kwargs)

        self.model = self.model.cuda()
        self.model.eval()
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])

    def preprocess(self, input: Input) -> Dict[str, Any]:

        img = LoadImage.convert_to_img(input)

        data = self.transform(img)
        data = collate([data], samples_per_gpu=1)
        if next(self.model.parameters()).is_cuda:
            # scatter to specified GPU
            data = scatter(data, [next(self.model.parameters()).device])[0]

        return data

    def forward(self, input: Dict[str, Any]) -> Dict[str, Any]:
        with torch.no_grad():
            # currently only support one task in pipeline
            results = self.model(input, task_name='seg-voc')
            return results

    def postprocess(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        return inputs
