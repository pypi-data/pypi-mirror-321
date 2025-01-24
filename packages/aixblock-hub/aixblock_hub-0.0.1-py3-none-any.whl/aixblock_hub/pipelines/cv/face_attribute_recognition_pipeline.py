# Copyright (c) AIxBlock, Inc. 
import os.path as osp
from typing import Any, Dict

import cv2
import numpy as np
import PIL
import torch

from aixblock_hub.metainfo import Pipelines
from aixblock_hub.models.cv.face_attribute_recognition import \
    FaceAttributeRecognition
from aixblock_hub.models.cv.face_recognition.align_face import align_face
from aixblock_hub.outputs import OutputKeys
from aixblock_hub.pipelines import pipeline
from aixblock_hub.pipelines.base import Input, Pipeline
from aixblock_hub.pipelines.builder import PIPELINES
from aixblock_hub.preprocessors import LoadImage
from aixblock_hub.utils.constant import ModelFile, Tasks
from aixblock_hub.utils.logger import get_logger
from . import FaceProcessingBasePipeline

logger = get_logger()


@PIPELINES.register_module(
    Tasks.face_attribute_recognition,
    module_name=Pipelines.face_attribute_recognition)
class FaceAttributeRecognitionPipeline(FaceProcessingBasePipeline):

    def __init__(self, model: str, **kwargs):
        """
        use `model` to create a face attribute recognition pipeline for prediction
        Args:
            model: model id on aixblock hub.
        """
        super().__init__(model=model, **kwargs)
        ckpt_path = osp.join(model, ModelFile.TORCH_MODEL_FILE)
        logger.info(f'loading model from {ckpt_path}')
        device = torch.device(
            f'cuda:{0}' if torch.cuda.is_available() else 'cpu')
        fairface = FaceAttributeRecognition(
            model_path=ckpt_path, device=device)
        self.fairface = fairface
        self.device = device
        logger.info('load model done')

        male_list = ['Male', 'Female']
        age_list = [
            '0-2', '3-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69',
            '70+'
        ]
        self.map_list = [male_list, age_list]

    def preprocess(self, input: Input) -> Dict[str, Any]:
        result = super().preprocess(input)
        if result is None:
            rtn_dict = {}
            rtn_dict['img'] = None
            return rtn_dict
        return result

    def forward(self, input: Dict[str, Any]) -> Dict[str, Any]:
        if input['img'] is None:
            return {OutputKeys.SCORES: None, OutputKeys.LABELS: None}
        scores = self.fairface(input['img'])
        assert scores is not None
        return {OutputKeys.SCORES: scores, OutputKeys.LABELS: self.map_list}

    def postprocess(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        return inputs
