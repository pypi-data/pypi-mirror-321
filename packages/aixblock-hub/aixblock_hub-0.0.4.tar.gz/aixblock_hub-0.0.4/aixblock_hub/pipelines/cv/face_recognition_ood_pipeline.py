# Copyright (c) AIxBlock, Inc. 
import os.path as osp
from typing import Any, Dict

import cv2
import numpy as np
import PIL
import torch

from aixblock_hub.metainfo import Pipelines
from aixblock_hub.models import Model
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
    Tasks.face_recognition, module_name=Pipelines.face_recognition_ood)
class FaceRecognitionOodPipeline(FaceProcessingBasePipeline):

    def __init__(self, model: str, **kwargs):
        """
        use `model` to create a face recognition ood pipeline for prediction
        Args:
            model: model id on aixblock hub.

        Examples:

        >>> from aixblock_hub.pipelines import pipeline
        >>> fr_ood= pipeline('face-recognition-ood', 'damo/cv_ir_face-recognition-ood_rts')
        >>> fr_ood("https://app.aixblock.io/test/images/face_recognition_1.png")
        {{'img_embedding': array([[ 0.02276129, -0.00761525, ...,0.05735306]],
            dtype=float32, 'scores': [[0.7656678557395935]]}
        """

        # face recong model
        super().__init__(model=model, **kwargs)
        face_model = self.model
        face_model = face_model.to(self.device)
        face_model.eval()
        self.face_model = face_model
        logger.info('face recognition model loaded!')

    def preprocess(self, input: Input) -> Dict[str, Any]:
        result = super().preprocess(input)
        if result is None:
            rtn_dict = {}
            rtn_dict['img'] = None
            return rtn_dict
        align_img = result['img']
        face_img = align_img[:, :, ::-1]  # to rgb
        face_img = np.transpose(face_img, axes=(2, 0, 1))
        face_img = (face_img / 255. - 0.5) / 0.5
        face_img = face_img.astype(np.float32)
        result['img'] = face_img
        return result

    def forward(self, input: Dict[str, Any]) -> Dict[str, Any]:
        if input['img'] is None:
            return {OutputKeys.IMG_EMBEDDING: None, OutputKeys.SCORES: None}
        img = input['img'].unsqueeze(0)
        output = self.face_model(img)
        emb = output[0].detach().cpu().numpy()
        emb /= np.sqrt(np.sum(emb**2, -1, keepdims=True))  # l2 norm
        scores = output[1].exp().detach().cpu().numpy().tolist()
        return {OutputKeys.IMG_EMBEDDING: emb, OutputKeys.SCORES: scores}

    def postprocess(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        return inputs
