# Copyright (c) AIxBlock, Inc. 

import io
from typing import Any, Dict

import numpy
import soundfile as sf
import torch

from aixblock_hub.fileio import File
from aixblock_hub.metainfo import Models, Pipelines
from aixblock_hub.models.base import Input
from aixblock_hub.outputs import OutputKeys
from aixblock_hub.pipelines import Pipeline
from aixblock_hub.pipelines.builder import PIPELINES
from aixblock_hub.utils.constant import Tasks
from aixblock_hub.utils.logger import get_logger

logger = get_logger()


@PIPELINES.register_module(
    Tasks.speech_separation,
    module_name=Models.speech_mossformer_separation_temporal_8k)
@PIPELINES.register_module(
    Tasks.speech_separation,
    module_name=Models.speech_mossformer2_separation_temporal_8k)
class SeparationPipeline(Pipeline):

    def __init__(self, model, **kwargs):
        """create a speech separation pipeline for prediction

        Args:
            model: model id on aixblock hub.
        """
        logger.info('loading model...')
        super().__init__(model=model, **kwargs)
        self.model.load_check_point(device=self.device)
        self.model.eval()

    def preprocess(self, inputs: Input, **preprocess_params) -> Dict[str, Any]:
        if isinstance(inputs, str):
            file_bytes = File.read(inputs)
            data, fs = sf.read(io.BytesIO(file_bytes), dtype='float32')
            if fs != 8000:
                raise ValueError(
                    'aixblock error: The audio sample rate should be 8000')
        elif isinstance(inputs, bytes):
            data = torch.from_numpy(
                numpy.frombuffer(inputs, dtype=numpy.float32))
        return dict(data=data)

    def postprocess(self, inputs: Dict[str, Any],
                    **post_params) -> Dict[str, Any]:
        return inputs

    def forward(
        self, inputs: Dict[str, Any], **forward_params
    ) -> Dict[str, Any]:  # mix, targets, stage, noise=None):
        """Forward computations from the mixture to the separated signals."""
        logger.info('Start forward...')
        # Unpack lists and put tensors in the right device
        mix = inputs['data'].to(self.device)
        mix = torch.unsqueeze(mix, dim=1).transpose(0, 1)
        est_source = self.model(mix)
        result = []
        for ns in range(self.model.num_spks):
            signal = est_source[0, :, ns]
            signal = signal / signal.abs().max() * 0.5
            signal = signal.unsqueeze(0).cpu()
            # convert tensor to pcm
            output = (signal.numpy() * 32768).astype(numpy.int16).tobytes()
            result.append(output)
        logger.info('Finish forward.')
        return {OutputKeys.OUTPUT_PCM_LIST: result}
