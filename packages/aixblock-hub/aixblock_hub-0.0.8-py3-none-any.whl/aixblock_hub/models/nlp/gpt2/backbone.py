# Copyright (c) AIxBlock, Inc. 
from transformers import GPT2Config
from transformers import GPT2Model as GPT2ModelTransform

from aixblock_hub.metainfo import Models
from aixblock_hub.models.builder import BACKBONES
from aixblock_hub.utils.constant import Tasks


@BACKBONES.register_module(group_key=Tasks.backbone, module_name=Models.gpt2)
class GPT2Model(GPT2ModelTransform):

    def __init__(self, **kwargs):
        config = GPT2Config(**kwargs)
        super().__init__(config)
