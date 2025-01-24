# Copyright (c) AIxBlock, Inc. 

import math
import os.path as osp
from typing import Any, Dict

from aixblock_hub.metainfo import Pipelines
from aixblock_hub.models.cv.action_detection import ActionDetONNX
from aixblock_hub.outputs import OutputKeys
from aixblock_hub.pipelines.base import Input, Pipeline
from aixblock_hub.pipelines.builder import PIPELINES
from aixblock_hub.utils.config import Config
from aixblock_hub.utils.constant import ModelFile, Tasks
from aixblock_hub.utils.logger import get_logger

logger = get_logger()


@PIPELINES.register_module(
    Tasks.action_detection, module_name=Pipelines.action_detection)
class ActionDetectionPipeline(Pipeline):

    def __init__(self, model: str, **kwargs):
        """
        use `model` to create a action detection pipeline for prediction
        Args:
            model: model id on aixblock hub.
        """
        super().__init__(model=model, **kwargs)
        model_path = osp.join(self.model, ModelFile.ONNX_MODEL_FILE)
        logger.info(f'loading model from {model_path}')
        config_path = osp.join(self.model, ModelFile.CONFIGURATION)
        logger.info(f'loading config from {config_path}')
        self.cfg = Config.from_file(config_path)
        self.cfg.MODEL.model_file = model_path
        self.cfg.MODEL.update(kwargs)
        self.model = ActionDetONNX(self.model, self.cfg.MODEL,
                                   self.device_name)
        logger.info('load model done')

    def preprocess(self, input: Input) -> Dict[str, Any]:
        if isinstance(input, str):
            video_name = input
        else:
            raise TypeError(f'input should be a str,'
                            f'  but got {type(input)}')
        result = {'video_name': video_name}
        return result

    def forward(self, input: Dict[str, Any]) -> Dict[str, Any]:
        preds = self.model.forward(input['video_name'])
        labels = sum([pred['actions']['labels'] for pred in preds], [])
        scores = sum([pred['actions']['scores'] for pred in preds], [])
        boxes = sum([pred['actions']['boxes'] for pred in preds], [])
        timestamps = sum([[pred['timestamp']] * len(pred['actions']['labels'])
                          for pred in preds], [])
        out = {
            OutputKeys.TIMESTAMPS: timestamps,
            OutputKeys.LABELS: labels,
            OutputKeys.SCORES: scores,
            OutputKeys.BOXES: boxes
        }
        return out

    def postprocess(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        return inputs
