# Copyright (c) AIxBlock, Inc. 
import os.path as osp
from typing import Any, Dict

import cv2
import numpy as np
import PIL
import torch

from aixblock_hub.metainfo import Pipelines
from aixblock_hub.models.cv.face_detection import RetinaFaceDetection
from aixblock_hub.outputs import OutputKeys
from aixblock_hub.pipelines.base import Input, Pipeline
from aixblock_hub.pipelines.builder import PIPELINES
from aixblock_hub.preprocessors import LoadImage
from aixblock_hub.utils.constant import ModelFile, Tasks
from aixblock_hub.utils.logger import get_logger

logger = get_logger()


@PIPELINES.register_module(
    Tasks.face_detection, module_name=Pipelines.retina_face_detection)
class RetinaFaceDetectionPipeline(Pipeline):

    def __init__(self, model: str, **kwargs):
        """
        use `model` to create a face detection pipeline for prediction
        Args:
            model: model id on aixblock hub.
        """
        super().__init__(model=model, **kwargs)
        ckpt_path = osp.join(model, ModelFile.TORCH_MODEL_FILE)
        logger.info(f'loading model from {ckpt_path}')
        detector = RetinaFaceDetection(
            model_path=ckpt_path, device=self.device)
        self.detector = detector
        logger.info('load model done')

    def preprocess(self, input: Input) -> Dict[str, Any]:
        img = LoadImage.convert_to_ndarray(input)
        img = img.astype(np.float32)
        result = {'img': img}
        return result

    def forward(self, input: Dict[str, Any]) -> Dict[str, Any]:
        result = self.detector(input)
        assert result is not None
        bboxes = result[0][:, :4].tolist()
        scores = result[0][:, 4].tolist()
        lms = result[1].tolist()
        return {
            OutputKeys.SCORES: scores,
            OutputKeys.BOXES: bboxes,
            OutputKeys.KEYPOINTS: lms,
        }

    def postprocess(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        return inputs
