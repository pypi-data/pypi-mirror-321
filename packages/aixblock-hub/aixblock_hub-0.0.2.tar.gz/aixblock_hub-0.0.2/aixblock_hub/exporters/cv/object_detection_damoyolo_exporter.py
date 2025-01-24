# Copyright (c) AIxBlock, Inc. 
import os
from functools import partial
from typing import Mapping

import numpy as np
import onnx
import torch

from aixblock_hub.exporters.builder import EXPORTERS
from aixblock_hub.exporters.torch_model_exporter import TorchModelExporter
from aixblock_hub.metainfo import Models
from aixblock_hub.utils.constant import ModelFile, Tasks


@EXPORTERS.register_module(
    Tasks.domain_specific_object_detection,
    module_name=Models.tinynas_damoyolo)
@EXPORTERS.register_module(
    Tasks.image_object_detection, module_name=Models.tinynas_damoyolo)
class ObjectDetectionDamoyoloExporter(TorchModelExporter):

    def export_onnx(self,
                    output_dir: str,
                    opset=11,
                    input_shape=(1, 3, 640, 640)):
        onnx_file = os.path.join(output_dir, ModelFile.ONNX_MODEL_FILE)
        dummy_input = torch.randn(*input_shape)
        self.model.head.nms = False
        self.model.onnx_export = True
        self.model.eval()
        _ = self.model(dummy_input)
        torch.onnx._export(
            self.model,
            dummy_input,
            onnx_file,
            input_names=[
                'images',
            ],
            output_names=[
                'pred',
            ],
            opset_version=opset)

        return {'model', onnx_file}
