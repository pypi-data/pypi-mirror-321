# Copyright (c) AIxBlock, Inc. 
from transformers import BloomForCausalLM as BloomForCausalLMTransform

from aixblock_hub.metainfo import Models
from aixblock_hub.models import MODELS
from aixblock_hub.utils.constant import Tasks
from .backbone import MsModelMixin, TorchModel


@MODELS.register_module(
    group_key=Tasks.text_generation, module_name=Models.bloom)
class BloomForTextGeneration(MsModelMixin, BloomForCausalLMTransform,
                             TorchModel):

    pass
