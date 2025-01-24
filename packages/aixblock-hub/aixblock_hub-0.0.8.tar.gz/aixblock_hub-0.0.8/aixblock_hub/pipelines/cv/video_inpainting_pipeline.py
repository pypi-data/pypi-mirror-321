# Copyright 2021-2022 The Alibaba Fundamental Vision Team Authors. All rights reserved.
from typing import Any, Dict

from aixblock_hub.metainfo import Pipelines
from aixblock_hub.models.cv.video_inpainting import inpainting
from aixblock_hub.outputs import OutputKeys
from aixblock_hub.pipelines.base import Input, Pipeline
from aixblock_hub.pipelines.builder import PIPELINES
from aixblock_hub.utils.constant import Tasks
from aixblock_hub.utils.logger import get_logger

logger = get_logger()


@PIPELINES.register_module(
    Tasks.video_inpainting, module_name=Pipelines.video_inpainting)
class VideoInpaintingPipeline(Pipeline):

    def __init__(self, model: str, **kwargs):
        """
        use `model` to create video inpainting pipeline for prediction
        Args:
            model: model id on aixblock hub.
        """

        super().__init__(model=model, **kwargs)
        logger.info('load model done')

    def preprocess(self, input: Input) -> Dict[str, Any]:
        return input

    def forward(self, input: Dict[str, Any]) -> Dict[str, Any]:
        decode_error, fps, w, h = inpainting.video_process(
            input['video_input_path'])

        if decode_error is not None:
            return {OutputKeys.OUTPUT: 'decode_error'}

        inpainting.inpainting_by_model_balance(self.model,
                                               input['video_input_path'],
                                               input['mask_path'],
                                               input['video_output_path'], fps,
                                               w, h)

        return {OutputKeys.OUTPUT: 'Done'}

    def postprocess(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        return inputs
