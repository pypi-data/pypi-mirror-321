# Copyright (c) AIxBlock, Inc. 

from typing import Any, Dict

from aixblock_hub.metainfo import Pipelines
from aixblock_hub.pipelines.base import Input, Pipeline
from aixblock_hub.pipelines.builder import PIPELINES
from aixblock_hub.utils.constant import Tasks
from aixblock_hub.utils.device import device_placement
from aixblock_hub.utils.logger import get_logger

logger = get_logger()


@PIPELINES.register_module(
    Tasks.video_multi_modal_embedding,
    module_name=Pipelines.video_multi_modal_embedding)
class VideoMultiModalEmbeddingPipeline(Pipeline):

    def __init__(self, model: str, **kwargs):
        """
        use `model` to create a video_multi_modal_embedding pipeline for prediction
        Args:
            model: model id on aixblock hub.
        """
        super().__init__(model=model)

    def preprocess(self, input: Input) -> Dict[str, Any]:
        return input

    def _process_single(self, input: Input, *args, **kwargs) -> Dict[str, Any]:
        with device_placement(self.framework, self.device_name):
            out = self.forward(input)

        self._check_output(out)
        return out

    def forward(self, input: Dict[str, Any]) -> Dict[str, Any]:
        return self.model(input)

    def postprocess(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        return inputs
