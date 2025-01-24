# Copyright (c) AIxBlock, Inc. 

from typing import Any, Dict, Generator, Optional

import torch

from aixblock_hub.metainfo import Pipelines
from aixblock_hub.models.nlp import DistributedGPT3
from aixblock_hub.pipelines.base import DistributedPipeline
from aixblock_hub.pipelines.builder import PIPELINES
from aixblock_hub.preprocessors import TextGenerationJiebaPreprocessor
from aixblock_hub.utils.constant import Frameworks, Tasks
from aixblock_hub.utils.device import device_placement
from aixblock_hub.utils.streaming_output import PipelineStreamingOutputMixin


@PIPELINES.register_module(
    Tasks.text_generation, module_name=Pipelines.gpt3_generation)
class DistributedGPT3Pipeline(DistributedPipeline,
                              PipelineStreamingOutputMixin):
    """This class is used to instantiate the gpt3 model.
    """

    model = None

    def __init__(self, model, preprocessor=None, **kwargs):
        """

        Args:
            model: The model piece, str is not supported.
            preprocessor: The preprocessor matched with the model.
            kwargs (dict, `optional`):
                Extra kwargs passed into the preprocessor's constructor.
        """
        if preprocessor is None:
            preprocessor = TextGenerationJiebaPreprocessor(model)
        super().__init__(model, preprocessor=preprocessor, **kwargs)
        assert hasattr(preprocessor, 'tokenizer')
        self.model = PipelineStreamingOutputMixin()
        self._model_prepare = True

    @classmethod
    def _instantiate_one(cls, rank, model_dir, **kwargs):
        cls.model = DistributedGPT3(model_dir, rank, **kwargs)
        cls.model.eval()

    @classmethod
    def _forward_one(cls, inputs: Dict[str, Any]) -> Dict[str, Any]:
        tokens = inputs['inputs']['input_ids'].cuda(
            torch.cuda.current_device())
        return cls.model.generate(tokens, **inputs['forward_params'])

    def postprocess(self, inputs: Dict[str, Any],
                    **postprocess_params) -> Dict[str, str]:
        """process the prediction results

        Args:
            inputs (Dict[str, Any]): _description_

        Returns:
            Dict[str, str]: the prediction results
        """
        from aixblock_hub.outputs import OutputKeys
        return {
            OutputKeys.TEXT:
            self.preprocessor.tokenizer.detokenize(
                inputs.sequences[0].tolist())
        }

    def _sanitize_parameters(self, **pipeline_parameters):
        return {}, pipeline_parameters, {}

    def _stream_single(self, model_input: Dict[str, Any],
                       forward_params: Dict[str, Any],
                       postprocess_params: Dict[str, Any]) -> Generator:

        with device_placement(self.framework, self.device_name):
            if self._auto_collate:
                model_input = self._collate_fn(model_input)
            inputs = {'inputs': model_input, 'forward_params': forward_params}
            self.model_pool.map(self.__class__._stream_one,
                                [inputs] * self.world_size)

        while True:
            res = self.model_pool.map(self.__class__._next_one,
                                      range(self.world_size))
            if res[0] is None:
                break
            out = self.postprocess(res[0], **postprocess_params)
            self._check_output(out)
            yield out

    @classmethod
    def _stream_one(cls, inputs: Dict[str, Any]) -> None:
        tokens = inputs['inputs']['input_ids'].cuda(
            torch.cuda.current_device())
        cls._stream = cls.model.stream_generate(tokens,
                                                **inputs['forward_params'])

    @classmethod
    def _next_one(cls, idx: int) -> Optional[Dict[str, Any]]:
        try:
            return next(cls._stream)
        except StopIteration:
            return None
