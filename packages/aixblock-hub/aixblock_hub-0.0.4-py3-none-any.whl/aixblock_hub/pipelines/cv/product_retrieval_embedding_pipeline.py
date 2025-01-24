# Copyright (c) AIxBlock, Inc. 
import os.path as osp
from typing import Any, Dict

import cv2
import numpy as np
import torch
from PIL import Image
from torchvision import transforms

from aixblock_hub.metainfo import Pipelines
from aixblock_hub.pipelines.base import Input, Model, Pipeline
from aixblock_hub.pipelines.builder import PIPELINES
from aixblock_hub.preprocessors import LoadImage
from aixblock_hub.utils.constant import Tasks
from aixblock_hub.utils.logger import get_logger

logger = get_logger()


@PIPELINES.register_module(
    Tasks.product_retrieval_embedding,
    module_name=Pipelines.product_retrieval_embedding)
class ProductRetrievalEmbeddingPipeline(Pipeline):

    def __init__(self, model: str, **kwargs):
        """use `model` to create a pipeline for prediction
        Args:
            model: model id on aixblock hub.
        """
        super().__init__(model=model, **kwargs)

    def preprocess(self, input: Input) -> Dict[str, Any]:
        """
        preprocess the input image to cv2-bgr style
        """
        img = LoadImage.convert_to_ndarray(input)  # array with rgb
        img = np.ascontiguousarray(img[:, :, ::-1])  # array with bgr
        result = {'img': img}  # only for detection
        return result

    def forward(self, input: Dict[str, Any]) -> Dict[str, Any]:
        return self.model(input)

    def postprocess(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        return inputs
