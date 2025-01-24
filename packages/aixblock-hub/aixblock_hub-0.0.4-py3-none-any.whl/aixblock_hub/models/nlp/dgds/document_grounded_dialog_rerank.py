import os
from typing import Dict

import torch
from torch import nn

from aixblock_hub.metainfo import Models
from aixblock_hub.models.base import Model, Tensor, TorchModel
from aixblock_hub.models.builder import MODELS
from aixblock_hub.utils.config import Config
from aixblock_hub.utils.constant import ModelFile, Tasks
from .backbone import ClassifyRerank


@MODELS.register_module(
    Tasks.document_grounded_dialog_rerank, module_name=Models.doc2bot)
class DocumentGroundedDialogRerankModel(TorchModel):
    _backbone_prefix = ''

    def __init__(self, model_dir, **kwargs):
        super().__init__(model_dir, **kwargs)
        self.model = ClassifyRerank(model_dir)

    def forward(self, input: Dict[str, Tensor]):
        outputs = self.model(
            input_ids=input['input_ids'],
            attention_mask=input['attention_mask'])
        return outputs

    def resize_token_embeddings(self, size):
        self.model.base_model.resize_token_embeddings(size)

    def save_pretrained(self, addr):
        self.model.base_model.save_pretrained(addr)
