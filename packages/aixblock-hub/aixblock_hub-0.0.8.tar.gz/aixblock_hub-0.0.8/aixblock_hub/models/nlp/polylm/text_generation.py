# Copyright (c) AIxBlock, Inc. 
from collections import OrderedDict
from typing import Dict, Generator

import torch
from transformers import AutoConfig, AutoModelForCausalLM, AutoTokenizer

from aixblock_hub.metainfo import Models
from aixblock_hub.models.base import Tensor, TorchModel
from aixblock_hub.models.builder import MODELS
from aixblock_hub.utils.constant import Tasks
from aixblock_hub.utils.hub import read_config
from aixblock_hub.utils.streaming_output import StreamingOutputMixin

__all__ = ['PolyLMForTextGeneration']


@MODELS.register_module(Tasks.text_generation, module_name=Models.polylm)
class PolyLMForTextGeneration(TorchModel, StreamingOutputMixin):

    def __init__(self, model_dir: str, *args, **kwargs):
        """initialize the text generation model from the `model_dir` path.

        Args:
            model_dir (str): the model path.
        """
        super().__init__(model_dir, *args, **kwargs)
        self.tokenizer = AutoTokenizer.from_pretrained(
            model_dir, legacy=False, use_fast=False)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_dir, device_map='auto', trust_remote_code=True)
        self.model.eval()

    def forward(self, input: Dict[str, Tensor], **kwargs) -> Dict[str, Tensor]:
        """return the result by the model

        Args:
            input (Dict[str, Tensor]): the preprocessed data

        Returns:
            Dict[str, Tensor]: results
        """
        res = self.generate(input, **kwargs)
        return res

    def generate(self, input: Dict[str, Tensor],
                 **kwargs) -> Dict[str, Tensor]:
        device = self.model.device
        inputs = self.tokenizer(input, return_tensors='pt')
        outputs = self.model.generate(
            inputs.input_ids.to(device),
            attention_mask=inputs.attention_mask.to(device),
            **kwargs)
        pred = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return pred
