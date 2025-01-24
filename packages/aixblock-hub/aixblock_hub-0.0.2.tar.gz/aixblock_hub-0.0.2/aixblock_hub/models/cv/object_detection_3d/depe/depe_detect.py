# Copyright (c) AIxBlock, Inc. 
import os
import os.path as osp
from typing import Any, Dict, List, Union

import numpy as np
import torch

from aixblock_hub.metainfo import Models
from aixblock_hub.models.base import TorchModel
from aixblock_hub.models.builder import MODELS
from aixblock_hub.utils.config import Config
from aixblock_hub.utils.constant import ModelFile, Tasks
from aixblock_hub.utils.logger import get_logger

logger = get_logger()

__all__ = ['DepeDetect']


@MODELS.register_module(Tasks.object_detection_3d, module_name=Models.depe)
class DepeDetect(TorchModel):

    def __init__(self, model_dir: str, *args, **kwargs):
        """DEPE is a simple and pure DETR-like 3D detector with transformers,
        for more information please refer to:
        https://www.aixblock.io/models/damo/cv_object-detection-3d_depe/summary

        initialize the 3d object detection model from the `model_dir` path.
        Args:
            model_dir (str): the model path.
        """
        super().__init__(model_dir, *args, **kwargs)
        from mmcv.runner import load_checkpoint
        import aixblock_hub.models.cv.object_detection_3d.depe.mmdet3d_plugin
        from aixblock_hub.models.cv.object_detection_3d.depe.mmdet3d_plugin.models.detectors import Petr3D

        # build model and load checkpoint
        config_path = osp.join(model_dir, ModelFile.CONFIGURATION)
        config = Config.from_file(config_path)
        detector = Petr3D(**config.model.network_param)
        model_file = kwargs.get('model_file', ModelFile.TORCH_MODEL_BIN_FILE)
        ckpt_path = osp.join(model_dir, model_file)
        logger.info(f'loading model from {ckpt_path}')
        load_checkpoint(detector, ckpt_path, map_location='cpu')
        detector.eval()
        self.detector = detector
        logger.info('load model done')

    def forward(self, img: Union[torch.Tensor, List[torch.Tensor]],
                img_metas: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Args:
            img (`torch.Tensor`): batched image tensor or list of batched image tensor,
                shape of each tensor is [B, N, C, H, W], N is 12 for 6 views from current
                and history frame.
            img_metas (` List[Dict[str, Any]`): image meta info.
        Return:
            result (`List[Dict[str, Any]]`): list of detection results.
        """

        if isinstance(img, torch.Tensor):
            img = [img]
            img_metas = [img_metas]

        result = self.detector(
            return_loss=False, rescale=True, img=img, img_metas=img_metas)
        assert result is not None
        return result
