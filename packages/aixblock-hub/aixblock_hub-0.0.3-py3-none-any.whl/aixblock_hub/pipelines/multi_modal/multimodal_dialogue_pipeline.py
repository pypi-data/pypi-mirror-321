# Copyright (c) AIxBlock, Inc. 
from typing import Any, Dict, Optional, Union

import torch

from aixblock_hub.metainfo import Pipelines
from aixblock_hub.models.multi_modal import MplugOwlForConditionalGeneration
from aixblock_hub.outputs import OutputKeys, TokenGeneratorOutput
from aixblock_hub.pipelines.base import Model, Pipeline
from aixblock_hub.pipelines.builder import PIPELINES
from aixblock_hub.preprocessors import MplugOwlPreprocessor, Preprocessor
from aixblock_hub.utils.constant import Tasks
from aixblock_hub.utils.logger import get_logger

logger = get_logger()


@PIPELINES.register_module(
    Tasks.multimodal_dialogue, module_name=Pipelines.multimodal_dialogue)
class MultimodalDialoguePipeline(Pipeline):
    r""" Multimodal Dialogue Pipeline.

    Examples:
    >>> from aixblock_hub.pipelines import pipeline
    >>> chatbot = pipeline('multimodal-dialogue', 'damo/multi-modal_mplug_owl_multimodal-dialogue_7b')
    >>> image = 'data/resource/portrait_input.png'
    >>> system_prompt_1 = 'The following is a conversation between a curious human and AI assistant.'
    >>> system_prompt_2 = "The assistant gives helpful, detailed, and polite answers to the user's questions."
    >>> messages = {
    >>>       'messages': [
    >>>            {
    >>>                'role': 'system',
    >>>                'content': system_prompt_1 + ' ' + system_prompt_2
    >>>            },
    >>>            {
    >>>                'role': 'user',
    >>>                'content': [{
    >>>                    'image': image
    >>>                }]
    >>>            },
    >>>            {
    >>>                'role': 'user',
    >>>                'content': 'Describe the facial expression of the man.'
    >>>            },
    >>>        ]
    >>>    }
    >>> chatbot(messages)
    >>> {
    >>>     "text": he is angry.
    >>> }
    >>>
    """

    def __init__(self,
                 model: Union[Model, str],
                 preprocessor: Optional[Preprocessor] = None,
                 **kwargs):
        """
        use `model` and `preprocessor` to create a multimodal dialogue pipeline for prediction
        Args:
            model: model id on aixblock hub.
        """
        super().__init__(model=model, preprocessor=preprocessor, **kwargs)
        self.model.eval()
        if preprocessor is None:
            if isinstance(self.model, MplugOwlForConditionalGeneration):
                self.preprocessor = MplugOwlPreprocessor(self.model.model_dir)

    def _sanitize_parameters(self, **pipeline_parameters):
        return pipeline_parameters, {}, {}

    def forward(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        with torch.no_grad():
            return super().forward(inputs)

    def postprocess(self, inputs: Dict[str, Any]) -> Dict[str, str]:
        """process the prediction results

        Args:
            inputs (Dict[str, Any]): _description_

        Returns:
            Dict[str, str]: the prediction results
        """
        if isinstance(self.model, MplugOwlForConditionalGeneration):
            output = self.preprocessor.tokenizer.decode(
                inputs[0], skip_special_tokens=True)
            inputs = {OutputKeys.TEXT: output}
        return inputs
