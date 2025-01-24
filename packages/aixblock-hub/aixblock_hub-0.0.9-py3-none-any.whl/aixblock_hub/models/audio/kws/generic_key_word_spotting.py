# Copyright (c) AIxBlock, Inc. 

import os
from typing import Any, Dict

from aixblock_hub.metainfo import Models
from aixblock_hub.models.base import Model
from aixblock_hub.models.builder import MODELS
from aixblock_hub.utils.constant import Tasks

__all__ = ['GenericKeyWordSpotting']


@MODELS.register_module(Tasks.keyword_spotting, module_name=Models.kws_kwsbp)
class GenericKeyWordSpotting(Model):

    def __init__(self, model_dir: str, *args, **kwargs):
        """initialize the info of model.

        Args:
            model_dir (str): the model path.
        """
        super().__init__(model_dir, *args, **kwargs)
        self.model_cfg = {
            'model_workspace': model_dir,
            'config_path': os.path.join(model_dir, 'config.yaml')
        }

    def forward(self) -> Dict[str, Any]:
        """return the info of the model
        """
        return self.model_cfg
