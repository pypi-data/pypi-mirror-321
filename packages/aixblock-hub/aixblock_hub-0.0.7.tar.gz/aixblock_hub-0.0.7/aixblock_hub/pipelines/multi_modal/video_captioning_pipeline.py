# Copyright (c) AIxBlock, Inc. 
from typing import Any, Dict, Optional, Union

import torch

from aixblock_hub.metainfo import Pipelines
from aixblock_hub.models.multi_modal import HiTeAForAllTasks
from aixblock_hub.outputs import OutputKeys
from aixblock_hub.pipelines.base import Model, Pipeline
from aixblock_hub.pipelines.builder import PIPELINES
from aixblock_hub.preprocessors import HiTeAPreprocessor, Preprocessor
from aixblock_hub.utils.constant import Tasks
from aixblock_hub.utils.logger import get_logger

logger = get_logger()


@PIPELINES.register_module(
    Tasks.video_captioning, module_name=Pipelines.video_captioning)
class VideoCaptioningPipeline(Pipeline):

    def __init__(self,
                 model: Union[Model, str],
                 preprocessor: Optional[Preprocessor] = None,
                 **kwargs):
        """
        use `model` and `preprocessor` to create a video captioning pipeline for prediction
        Args:
            model: model id on aixblock hub.
        """
        super().__init__(model=model, preprocessor=preprocessor, **kwargs)
        self.model.eval()
        if preprocessor is None:
            if isinstance(self.model, HiTeAForAllTasks):
                self.preprocessor = HiTeAPreprocessor(self.model.model_dir)

    def _batch(self, data):
        if isinstance(self.model, HiTeAForAllTasks):
            from transformers.tokenization_utils_base import BatchEncoding
            batch_data = dict(train=data[0]['train'])
            batch_data['video'] = torch.cat([d['video'] for d in data])
            question = {}
            for k in data[0]['question'].keys():
                question[k] = torch.cat([d['question'][k] for d in data])
            batch_data['question'] = BatchEncoding(question)
            return batch_data
        else:
            return super()._collate_batch(data)

    def forward(self, inputs: Dict[str, Any],
                **forward_params) -> Dict[str, Any]:
        with torch.no_grad():
            return super().forward(inputs, **forward_params)

    def postprocess(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        return inputs
