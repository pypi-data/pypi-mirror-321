# Copyright 2021-2022 The Alibaba Fundamental Vision Team Authors. All rights reserved.
from typing import Any, Dict

import numpy as np

from aixblock_hub.metainfo import Pipelines
from aixblock_hub.models.cv.face_emotion import emotion_infer
from aixblock_hub.outputs import OutputKeys
from aixblock_hub.pipelines.base import Input, Pipeline
from aixblock_hub.pipelines.builder import PIPELINES
from aixblock_hub.preprocessors import LoadImage
from aixblock_hub.utils.constant import ModelFile, Tasks
from aixblock_hub.utils.logger import get_logger

logger = get_logger()


@PIPELINES.register_module(
    Tasks.face_emotion, module_name=Pipelines.face_emotion)
class FaceEmotionPipeline(Pipeline):

    def __init__(self, model: str, **kwargs):
        """
        use `model` to create face emotion pipeline for prediction
        Args:
            model: model id on aixblock hub.
        """

        super().__init__(model=model, **kwargs)
        self.face_model = model + '/' + ModelFile.TF_GRAPH_FILE
        logger.info('load model done')

    def preprocess(self, input: Input) -> Dict[str, Any]:
        img = LoadImage.convert_to_ndarray(input)
        return img

    def forward(self, input: Dict[str, Any]) -> Dict[str, Any]:
        result, bbox = emotion_infer.inference(input, self.model,
                                               self.face_model)
        return {OutputKeys.OUTPUT: result, OutputKeys.BOXES: bbox}

    def postprocess(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        return inputs
