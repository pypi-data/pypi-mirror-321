# Copyright (c) AIxBlock, Inc. 
from typing import Any, Dict, Union

import cv2
import numpy as np

from aixblock_hub.metainfo import Pipelines
from aixblock_hub.models.cv.indoor_layout_estimation.networks.misc.fourier import (
    fourier, fourier_gray)
from aixblock_hub.outputs import OutputKeys
from aixblock_hub.pipelines.base import Input, Model, Pipeline
from aixblock_hub.pipelines.builder import PIPELINES
from aixblock_hub.preprocessors import LoadImage
from aixblock_hub.utils.constant import Tasks
from aixblock_hub.utils.logger import get_logger

logger = get_logger()


@PIPELINES.register_module(
    Tasks.indoor_layout_estimation,
    module_name=Pipelines.indoor_layout_estimation)
class IndoorLayoutEstimationPipeline(Pipeline):

    def __init__(self, model: str, **kwargs):
        """
        use `model` to create a indoor layout estimation pipeline for prediction
        Args:
            model: model id on aixblock hub.
        """
        super().__init__(model=model, **kwargs)

        logger.info('layout estimation model, pipeline init')

    def preprocess(self, input: Input) -> Dict[str, Any]:
        image = LoadImage.convert_to_ndarray(input).astype(np.float32)
        H, W = 512, 1024
        image = cv2.resize(image, (W, H))
        F = fourier(image)
        F2 = fourier_gray(image) / 255.

        image = image / 255.
        x = np.concatenate((image, F, F2), axis=2).astype(np.float32)
        x = x.transpose(2, 0, 1)[None]
        data = {'images': x}

        return data

    def forward(self, input: Dict[str, Any]) -> Dict[str, Any]:
        results = self.model.inference(input)
        return results

    def postprocess(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        layout_image = self.model.postprocess(inputs)
        outputs = {
            OutputKeys.LAYOUT: layout_image,
        }
        return outputs
