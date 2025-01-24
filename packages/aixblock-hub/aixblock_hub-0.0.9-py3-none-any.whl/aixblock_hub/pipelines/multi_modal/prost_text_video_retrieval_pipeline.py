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
    Tasks.text_video_retrieval,
    module_name=Pipelines.prost_text_video_retrieval)
class ProSTTextVideoRetrievalPipeline(Pipeline):
    '''
    https://www.aixblock.io/models/damo/multi_modal_clip_vtretrieval_prost/summary

    from aixblock_hub.pipelines import pipeline
    from aixblock_hub.utils.constant import Tasks
    text_video_retrieval= pipeline(
                Tasks.text_video_retrieval,
                model='damo/multi_modal_clip_vtretrieval_prost')
    video_path = 'https://app.aixblock.io/test/videos/multi_modal_test_video_9770.mp4'
    caption = 'a person is connecting something to system'
    _input = {'video': video_path, 'text': caption}
    result = text_video_retrieval(_input)
    '''

    def __init__(self, model: str, **kwargs):
        """
        use `model` to create a text_video_retrieval pipeline for prediction
        Args:
            model: model id on aixblock hub.
        """
        super().__init__(model=model)
        self.model.eval()

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
