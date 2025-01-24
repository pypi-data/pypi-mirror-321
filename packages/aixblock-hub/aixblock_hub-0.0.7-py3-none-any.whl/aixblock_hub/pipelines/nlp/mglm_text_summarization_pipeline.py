# Copyright (c) 2022 Zhipu.AI

import os
from typing import Any, Dict, Optional, Union

from aixblock_hub.metainfo import Pipelines
from aixblock_hub.models.base import Model
from aixblock_hub.models.nlp import MGLMForTextSummarization
from aixblock_hub.pipelines.base import Pipeline, Tensor
from aixblock_hub.pipelines.builder import PIPELINES
from aixblock_hub.preprocessors import (MGLMSummarizationPreprocessor,
                                      Preprocessor)
from aixblock_hub.utils.constant import Tasks

__all__ = ['MGLMTextSummarizationPipeline']


@PIPELINES.register_module(
    group_key=Tasks.text_summarization,
    module_name=Pipelines.mglm_text_summarization)
class MGLMTextSummarizationPipeline(Pipeline):

    def __init__(self,
                 model: Union[MGLMForTextSummarization, str],
                 preprocessor: Optional[Preprocessor] = None,
                 *args,
                 **kwargs):
        model = MGLMForTextSummarization(model) if isinstance(model,
                                                              str) else model
        self.model = model
        self.model.eval()
        if preprocessor is None:
            preprocessor = MGLMSummarizationPreprocessor()
        from aixblock_hub.utils.torch_utils import _find_free_port
        os.environ['MASTER_PORT'] = str(_find_free_port())
        super().__init__(model=model, preprocessor=preprocessor, **kwargs)

    # define the forward pass
    def forward(self, inputs: Union[Dict, str],
                **forward_params) -> Dict[str, Any]:
        inputs = {'text': inputs} if isinstance(inputs, str) else inputs
        return self.model.generate(inputs)

    # format the outputs from pipeline
    def postprocess(self, input, **kwargs) -> Dict[str, Any]:
        return input
