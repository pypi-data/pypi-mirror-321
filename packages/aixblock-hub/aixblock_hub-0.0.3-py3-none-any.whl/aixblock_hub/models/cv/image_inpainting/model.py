# Copyright (c) AIxBlock, Inc. 
import os
from typing import Any, Dict, Optional, Union

import torch

from aixblock_hub.metainfo import Models
from aixblock_hub.models.base.base_torch_model import TorchModel
from aixblock_hub.models.builder import MODELS
from aixblock_hub.utils.constant import ModelFile, Tasks
from aixblock_hub.utils.logger import get_logger

LOGGER = get_logger()


@MODELS.register_module(
    Tasks.image_inpainting, module_name=Models.image_inpainting)
class FFTInpainting(TorchModel):

    def __init__(self, model_dir: str, **kwargs):
        super().__init__(model_dir, **kwargs)

        from .default import DefaultInpaintingTrainingModule
        pretrained = kwargs.get('pretrained', True)
        predict_only = kwargs.get('predict_only', False)
        net = DefaultInpaintingTrainingModule(
            model_dir=model_dir, predict_only=predict_only)
        if pretrained:
            path = os.path.join(model_dir, ModelFile.TORCH_MODEL_FILE)
            LOGGER.info(f'loading pretrained model from {path}')
            state = torch.load(path, map_location='cpu')
            net.load_state_dict(state, strict=False)
        self.model = net

    def forward(self, inputs):
        return self.model(inputs)
