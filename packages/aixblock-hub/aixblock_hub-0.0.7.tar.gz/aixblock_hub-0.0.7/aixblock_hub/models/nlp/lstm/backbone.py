# Copyright (c) AIxBlock, Inc. 
"""PyTorch LSTM model. """

import torch.nn as nn

from aixblock_hub.metainfo import Models
from aixblock_hub.models import TorchModel
from aixblock_hub.models.builder import MODELS
from aixblock_hub.outputs import BackboneModelOutput
from aixblock_hub.utils.constant import Tasks


@MODELS.register_module(group_key=Tasks.backbone, module_name=Models.lstm)
class LSTMModel(TorchModel):

    def __init__(self, vocab_size, embed_width, hidden_size=100, **kwargs):
        super().__init__()
        hidden_size = kwargs.get('lstm_hidden_size', hidden_size)
        self.embedding = Embedding(vocab_size, embed_width)
        self.lstm = nn.LSTM(
            embed_width,
            hidden_size,
            num_layers=1,
            bidirectional=True,
            batch_first=True)

    def forward(self, input_ids, **kwargs) -> BackboneModelOutput:
        embedding = self.embedding(input_ids)
        lstm_output, _ = self.lstm(embedding)
        return BackboneModelOutput(last_hidden_state=lstm_output)


class Embedding(nn.Module):

    def __init__(self, vocab_size, embed_width):
        super(Embedding, self).__init__()

        self.embedding = nn.Embedding(vocab_size, embed_width)

    def forward(self, input_ids):
        return self.embedding(input_ids)
