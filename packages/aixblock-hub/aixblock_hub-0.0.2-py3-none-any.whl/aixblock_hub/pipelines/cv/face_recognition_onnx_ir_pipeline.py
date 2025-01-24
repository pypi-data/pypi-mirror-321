# Copyright (c) AIxBlock, Inc. 
import os.path as osp
from typing import Any, Dict

import cv2
import numpy as np
import onnxruntime
import PIL
import torch
import torch.nn.functional as F

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
    Tasks.face_recognition, module_name=Pipelines.face_recognition_onnx_ir)
class FaceRecognitionOnnxIrPipeline(FaceProcessingBasePipeline):

    def __init__(self, model: str, **kwargs):
        """
        FaceRecognitionOnnxIrPipeline  can extract 512-dim feature of IR face image.
        use `model` to create a face recognition ir onnx pipeline for prediction.
        Args:
            model: model id on aixblock hub.
        Example:

        >>> from aixblock_hub.pipelines import pipeline
        >>> frir = pipeline('face-recognition-ood', 'damo/cv_manual_face-recognition_frir')
        >>> frir("https://app.aixblock.io/test/images/ir_face_recognition_1.png")
        >>> # {{'img_embedding': array([[ 0.02276129, -0.00761525, ...,0.05735306]], dtype=float32)} }
        """
        super().__init__(model=model, **kwargs)
        onnx_path = osp.join(model, ModelFile.ONNX_MODEL_FILE)
        logger.info(f'loading model from {onnx_path}')
        self.sess, self.input_node_name, self.out_node_name = self.load_onnx_model(
            onnx_path)
        logger.info('load model done')

    def load_onnx_model(self, onnx_path):
        sess = onnxruntime.InferenceSession(
            onnx_path,
            providers=['CUDAExecutionProvider', 'CPUExecutionProvider'])
        out_node_name = []
        input_node_name = []
        for node in sess.get_outputs():
            out_node_name.append(node.name)

        for node in sess.get_inputs():
            input_node_name.append(node.name)

        return sess, input_node_name, out_node_name

    def preprocess(self, input: Input) -> Dict[str, Any]:
        result = super().preprocess(input)
        if result is None:
            rtn_dict = {}
            rtn_dict['input_tensor'] = None
            return rtn_dict
        align_img = result['img']
        face_img = align_img[:, :, ::-1]  # to rgb
        face_img = (face_img / 255. - 0.5) / 0.5
        face_img = np.expand_dims(face_img, 0).copy()
        face_img = np.transpose(face_img, axes=(0, 3, 1, 2))
        face_img = face_img.astype(np.float32)
        result['input_tensor'] = face_img
        return result

    def forward(self, input: Dict[str, Any]) -> Dict[str, Any]:
        if input['input_tensor'] is None:
            return {OutputKeys.IMG_EMBEDDING: None}
        input_feed = {}
        input_feed[
            self.input_node_name[0]] = input['input_tensor'].cpu().numpy()
        emb = self.sess.run(self.out_node_name, input_feed=input_feed)[0]
        emb /= np.sqrt(np.sum(emb**2, -1, keepdims=True))  # l2 norm
        return {OutputKeys.IMG_EMBEDDING: emb}

    def postprocess(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        return inputs
