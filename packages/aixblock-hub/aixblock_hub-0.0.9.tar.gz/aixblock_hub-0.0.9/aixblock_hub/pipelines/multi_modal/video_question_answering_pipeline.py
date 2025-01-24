# Copyright (c) AIxBlock, Inc. 
from typing import Any, Dict, Optional, Union

import torch

from aixblock_hub.metainfo import Pipelines
from aixblock_hub.models import Model
from aixblock_hub.models.multi_modal import HiTeAForAllTasks
from aixblock_hub.outputs import OutputKeys
from aixblock_hub.pipelines.base import Pipeline, Tensor
from aixblock_hub.pipelines.builder import PIPELINES
from aixblock_hub.preprocessors import HiTeAPreprocessor, Preprocessor
from aixblock_hub.utils.constant import Tasks

__all__ = ['VideoQuestionAnsweringPipeline']


@PIPELINES.register_module(
    Tasks.video_question_answering,
    module_name=Pipelines.video_question_answering)
class VideoQuestionAnsweringPipeline(Pipeline):

    def __init__(self,
                 model: Union[Model, str],
                 preprocessor: Optional[Preprocessor] = None,
                 **kwargs):
        """use `model` and `preprocessor` to create a video question answering pipeline for prediction

        Args:
            model (HiTeAForVideoQuestionAnswering): a model instance
            preprocessor (HiTeAForVideoQuestionAnsweringPreprocessor): a preprocessor instance
        """
        super().__init__(model=model, preprocessor=preprocessor, **kwargs)
        if preprocessor is None:
            if isinstance(self.model, HiTeAForAllTasks):
                self.preprocessor = HiTeAPreprocessor(self.model.model_dir)
        self.model.eval()

    def forward(self, inputs: Dict[str, Any],
                **forward_params) -> Dict[str, Any]:
        with torch.no_grad():
            return super().forward(inputs, **forward_params)

    def postprocess(self, inputs: Dict[str, Tensor],
                    **postprocess_params) -> Dict[str, str]:
        """process the prediction results

        Args:
            inputs (Dict[str, Any]): _description_

        Returns:
            Dict[str, str]: the prediction results
        """
        return inputs
