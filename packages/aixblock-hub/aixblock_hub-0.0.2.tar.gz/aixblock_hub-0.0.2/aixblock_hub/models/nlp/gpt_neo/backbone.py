# Copyright (c) AIxBlock, Inc. 
from transformers import GPTNeoConfig
from transformers import GPTNeoModel as GPTNeoModelTransform

from aixblock_hub.metainfo import Models
from aixblock_hub.models.builder import BACKBONES
from aixblock_hub.utils.constant import Tasks


@BACKBONES.register_module(
    group_key=Tasks.backbone, module_name=Models.gpt_neo)
class GPTNeoModel(GPTNeoModelTransform):

    def __init__(self, **kwargs):
        config = GPTNeoConfig(**kwargs)
        super().__init__(config)
