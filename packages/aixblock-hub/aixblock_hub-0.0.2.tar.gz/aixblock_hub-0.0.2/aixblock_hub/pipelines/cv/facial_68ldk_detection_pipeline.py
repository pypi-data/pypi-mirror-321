# Copyright (c) AIxBlock, Inc. 
import argparse
import os
from typing import Any, Dict, Union

import cv2
import numpy as np
import torch

from aixblock_hub.metainfo import Pipelines
from aixblock_hub.models.cv.facial_68ldk_detection import infer
from aixblock_hub.outputs import OutputKeys
from aixblock_hub.pipelines.base import Input, Model, Pipeline
from aixblock_hub.pipelines.builder import PIPELINES
from aixblock_hub.preprocessors import LoadImage
from aixblock_hub.utils.constant import ModelFile, Tasks
from aixblock_hub.utils.logger import get_logger

logger = get_logger()


@PIPELINES.register_module(
    Tasks.facial_68ldk_detection, module_name=Pipelines.facial_68ldk_detection)
class FaceLandmarkDetectionPipeline(Pipeline):

    def __init__(self, model: str, **kwargs):
        """
        use `model` to create a image depth prediction pipeline for prediction
        Args:
            model: model id on aixblock hub.
        """
        super().__init__(model=model, **kwargs)

        parser = argparse.ArgumentParser(description='Evaluation script')
        args = parser.parse_args()
        args.config_name = 'alignment'

        device_ids = list()
        if torch.cuda.is_available():
            device_ids = [0]
        else:
            device_ids = [-1]

        model_path = os.path.join(model, 'pytorch_model.pkl')

        self.fld = infer.Alignment(
            args, model_path, dl_framework='pytorch', device_ids=device_ids)

        logger.info('Face 2d landmark detection model, pipeline init')

    def preprocess(self, input: Input) -> Dict[str, Any]:
        print('start preprocess')

        image = LoadImage.convert_to_ndarray(input)
        image = cv2.resize(image, (256, 256))

        data = {'image': image}

        print('finish preprocess')

        return data

    def forward(self, input: Dict[str, Any]) -> Dict[str, Any]:
        print('start infer')

        image = input['image']

        if torch.cuda.is_available():
            image_np = image.cpu().numpy()
        else:
            image_np = image.numpy()

        x1, y1, x2, y2 = 0, 0, 256, 256
        scale = max(x2 - x1, y2 - y1) / 180
        center_w = (x1 + x2) / 2
        center_h = (y1 + y2) / 2
        scale, center_w, center_h = float(scale), float(center_w), float(
            center_h)

        results = self.fld.analyze(image_np, scale, center_w, center_h)

        print('finish infer')

        return results

    def postprocess(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        outputs = {'landmarks': inputs}
        return outputs
