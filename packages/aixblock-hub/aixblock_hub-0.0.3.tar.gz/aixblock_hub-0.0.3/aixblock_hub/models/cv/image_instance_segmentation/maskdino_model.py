# Copyright (c) AIxBlock, Inc. 
import os
from typing import Any, Dict

import torch

from aixblock_hub.metainfo import Models
from aixblock_hub.models.base import TorchModel
from aixblock_hub.models.builder import MODELS
from aixblock_hub.models.cv.image_instance_segmentation import MaskDINOSwin
from aixblock_hub.utils.config import Config
from aixblock_hub.utils.constant import ModelFile, Tasks


@MODELS.register_module(
    Tasks.image_segmentation, module_name=Models.maskdino_swin)
class MaskDINOSwinModel(TorchModel):

    def __init__(self, model_dir=None, *args, **kwargs):
        """
        Args:
            model_dir (str): model directory.
        """
        super(MaskDINOSwinModel, self).__init__(
            model_dir=model_dir, *args, **kwargs)

        if 'backbone' not in kwargs:
            config_path = os.path.join(model_dir, ModelFile.CONFIGURATION)
            cfg = Config.from_file(config_path)
            model_cfg = cfg.model
            kwargs.update(model_cfg)

        self.model = MaskDINOSwin(model_dir=model_dir, **kwargs)

        self.device = torch.device(
            'cuda' if torch.cuda.is_available() else 'cpu')
        self.model.to(self.device)

    def forward(self, input: Dict[str, Any]) -> Dict[str, Any]:
        output = self.model(**input)
        return output

    def postprocess(self, input: Dict[str, Any], **kwargs) -> Dict[str, Any]:
        return input
