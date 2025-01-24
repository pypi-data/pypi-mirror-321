# Copyright (c) AIxBlock, Inc. 
import os.path as osp
from typing import Any, Dict

import cv2
import numpy as np
import PIL
import torch

from aixblock_hub.metainfo import Pipelines
from aixblock_hub.models.cv.face_recognition.align_face import align_face
from aixblock_hub.models.cv.facial_landmark_confidence import \
    FacialLandmarkConfidence
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
    Tasks.face_2d_keypoints, module_name=Pipelines.facial_landmark_confidence)
class FacialLandmarkConfidencePipeline(FaceProcessingBasePipeline):

    def __init__(self, model: str, **kwargs):
        """
        use `model` to create a facial landmrk confidence pipeline for prediction
        Args:
            model: model id on aixblock hub.
        """
        super().__init__(model=model, **kwargs)
        ckpt_path = osp.join(model, ModelFile.TORCH_MODEL_FILE)
        logger.info(f'loading model from {ckpt_path}')
        flcm = FacialLandmarkConfidence(
            model_path=ckpt_path, device=self.device)
        self.flcm = flcm
        logger.info('load model done')

    def preprocess(self, input: Input) -> Dict[str, Any]:

        result = super().preprocess(input)
        if result is None:
            rtn_dict = {}
            rtn_dict['img'] = None
            return rtn_dict
        img = LoadImage.convert_to_ndarray(input)
        img = img[:, :, ::-1]
        result['orig_img'] = img.astype(np.float32)
        return result

    def forward(self, input: Dict[str, Any]) -> Dict[str, Any]:
        if input['img'] is None:
            return {
                OutputKeys.SCORES: None,
                OutputKeys.POSES: None,
                OutputKeys.KEYPOINTS: None,
                OutputKeys.BOXES: None
            }
        result = self.flcm(input)
        assert result is not None
        lms = result[0].reshape(-1, 10).tolist()
        scores = [1 - result[1].tolist()]
        boxes = input['bbox'].cpu().numpy()[np.newaxis, :].tolist()
        output_poses = []
        return {
            OutputKeys.SCORES: scores,
            OutputKeys.POSES: output_poses,
            OutputKeys.KEYPOINTS: lms,
            OutputKeys.BOXES: boxes
        }

    def postprocess(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        return inputs
