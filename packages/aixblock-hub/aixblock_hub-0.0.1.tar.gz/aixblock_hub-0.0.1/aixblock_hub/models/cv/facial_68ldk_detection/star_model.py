# Copyright (c) AIxBlock, Inc. 
import os

import cv2
import matplotlib.pyplot as plt
import numpy as np
import torch

from aixblock_hub.metainfo import Models
from aixblock_hub.models.base.base_torch_model import TorchModel
from aixblock_hub.models.builder import MODELS
from aixblock_hub.models.cv.facial_68ldk_detection import infer
from aixblock_hub.outputs import OutputKeys
from aixblock_hub.preprocessors import LoadImage
from aixblock_hub.utils.constant import ModelFile, Tasks
from aixblock_hub.utils.logger import get_logger

logger = get_logger()


@MODELS.register_module(
    Tasks.facial_68ldk_detection, module_name=Models.star_68ldk_detection)
class FaceLandmarkDetection(TorchModel):

    def __init__(self, model_dir, *args, **kwargs):
        super().__init__(model_dir, *args, **kwargs)

    def forward(self, Inputs):
        return Inputs

    def postprocess(self, Inputs):
        return Inputs

    def inference(self, data):
        return data
