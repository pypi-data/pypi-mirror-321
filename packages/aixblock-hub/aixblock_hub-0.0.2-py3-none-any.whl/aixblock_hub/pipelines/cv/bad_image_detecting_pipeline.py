# Copyright (c) AIxBlock, Inc. 
from typing import Any, Dict, Optional, Union

import numpy as np
import torch

from aixblock_hub.metainfo import Pipelines
from aixblock_hub.models.cv.bad_image_detecting import BadImageDetecting
from aixblock_hub.outputs import OutputKeys
from aixblock_hub.pipelines.base import Input, Pipeline
from aixblock_hub.pipelines.builder import PIPELINES
from aixblock_hub.preprocessors import LoadImage
from aixblock_hub.utils.constant import Tasks
from aixblock_hub.utils.logger import get_logger

logger = get_logger()

__all__ = ['BadImageDetecingPipeline']


@PIPELINES.register_module(
    Tasks.bad_image_detecting, module_name=Pipelines.bad_image_detecting)
class BadImageDetecingPipeline(Pipeline):
    """ Image Restoration Pipeline .

    Take bad_image_detecting as an example
    ```python
    >>> from aixblock_hub.pipelines import pipeline
    >>> image_pipeline = pipeline(Tasks.bad_image_detecting, model=model_id)
    >>> image_pipeline("https://app.aixblock.io/test/images/dogs.jpg")

    ```
    """

    def __init__(self, model: Union[BadImageDetecting, str], **kwargs):
        """
        use `model` and `preprocessor` to create a cv image denoise pipeline for prediction
        Args:
            model: model id on aixblock hub.
        """
        super().__init__(model=model, **kwargs)
        self.model.eval()
        self.labels = ['正常', '花屏', '绿屏']

        if torch.cuda.is_available():
            self._device = torch.device('cuda')
        else:
            self._device = torch.device('cpu')
        logger.info('load bad image detecting model done')

    def preprocess(self, input: Input) -> Dict[str, Any]:

        img = LoadImage.convert_to_ndarray(input)
        result = self.preprocessor(img)
        return result

    def forward(self, input: Dict[str, Any]) -> Dict[str, Any]:

        with torch.no_grad():
            output = self.model(input)  # output Tensor

        return {'output': output['output']}

    def postprocess(self, input: Dict[str, Any]) -> Dict[str, Any]:

        pred = input['output']
        score = torch.softmax(pred, dim=1).cpu().numpy()

        pred_scores = np.sort(score, axis=1)[0][::-1]
        pred_labels = np.argsort(score, axis=1)[0][::-1]
        result = {
            'pred_score': [score for score in pred_scores],
            'pred_class': [self.labels[label] for label in pred_labels]
        }

        outputs = {
            OutputKeys.SCORES: result['pred_score'],
            OutputKeys.LABELS: result['pred_class']
        }

        return outputs
