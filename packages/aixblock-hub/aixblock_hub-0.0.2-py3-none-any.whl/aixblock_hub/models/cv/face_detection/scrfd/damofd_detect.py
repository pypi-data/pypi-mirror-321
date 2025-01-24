# Copyright (c) AIxBlock, Inc. 
import os.path as osp
from copy import deepcopy
from typing import Any, Dict

import torch

from aixblock_hub.metainfo import Models
from aixblock_hub.models.base import TorchModel
from aixblock_hub.models.builder import MODELS
from aixblock_hub.outputs import OutputKeys
from aixblock_hub.utils.constant import ModelFile, Tasks
from aixblock_hub.utils.logger import get_logger
from .scrfd_detect import ScrfdDetect

logger = get_logger()

__all__ = ['DamoFdDetect']


@MODELS.register_module(Tasks.face_detection, module_name=Models.damofd)
class DamoFdDetect(ScrfdDetect):

    def __init__(self, model_dir, *args, **kwargs):
        """
        initialize the tinymog face detection model from the `model_dir` path.
        """
        config_file = 'DamoFD_lms.py'
        kwargs['config_file'] = config_file
        kwargs['model_file'] = ModelFile.TORCH_MODEL_FILE
        super().__init__(model_dir, **kwargs)
