# Copyright 2021-2022 The Alibaba Fundamental Vision Team Authors. All rights reserved.
from typing import Any, Dict

from aixblock_hub.metainfo import Pipelines
from aixblock_hub.pipelines.base import Input, Model, Pipeline
from aixblock_hub.pipelines.builder import PIPELINES
from aixblock_hub.utils.constant import Tasks
from aixblock_hub.utils.logger import get_logger

logger = get_logger()


@PIPELINES.register_module(
    Tasks.multi_modal_similarity, module_name=Pipelines.multi_modal_similarity)
class TEAMMultiModalSimilarityPipeline(Pipeline):

    def __init__(self, model: str, **kwargs):
        """
        use `model` to create a multimodal similarity pipeline
        Args:
            model: model id on aixblock hub.
        """
        super().__init__(model=model, **kwargs)

    def preprocess(self, input: Input) -> Dict[str, Any]:
        return input

    def forward(self, input: Dict[str, Any]) -> Dict[str, Any]:
        return self.model(input)

    def postprocess(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        return inputs
