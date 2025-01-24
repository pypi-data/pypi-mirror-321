# Copyright (c) AIxBlock, Inc. 
import os
import shutil
from tempfile import TemporaryDirectory
from typing import Any, Dict, Union

from aixblock_hub.metainfo import Pipelines
from aixblock_hub.outputs import OutputKeys
from aixblock_hub.pipelines.base import Input, Model, Pipeline
from aixblock_hub.pipelines.builder import PIPELINES
from aixblock_hub.utils.constant import Tasks
from aixblock_hub.utils.cv.image_utils import depth_to_color
from aixblock_hub.utils.logger import get_logger

logger = get_logger()


@PIPELINES.register_module(
    Tasks.image_multi_view_depth_estimation,
    module_name=Pipelines.image_multi_view_depth_estimation)
class ImageMultiViewDepthEstimationPipeline(Pipeline):

    def __init__(self, model: str, **kwargs):
        """
        use `model` to create a image multi-view depth estimation pipeline for prediction
        Args:
            model: model id on aixblock hub.
        """
        super().__init__(model=model, **kwargs)
        self.tmp_dir = None
        logger.info('pipeline init done')

    def check_input(self, input_dir):
        assert os.path.exists(
            input_dir), f'input dir:{input_dir} does not exsit'
        sub_dirs = os.listdir(input_dir)
        assert 'images' in sub_dirs, "must contain 'images' folder"
        assert 'sparse' in sub_dirs, "must contain 'sparse' folder"
        files = os.listdir(os.path.join(input_dir, 'sparse'))
        assert 'cameras.bin' in files, "'sparse' folder must contain 'cameras.bin'"
        assert 'images.bin' in files, "'sparse' folder must contain 'images.bin'"
        assert 'points3D.bin' in files, "'sparse' folder must contain 'points3D.bin'"

    def preprocess(self, input: Input) -> Dict[str, Any]:
        assert isinstance(input, str), 'input must be str'
        self.check_input(input)
        self.tmp_dir = TemporaryDirectory()

        casmvs_inp_dir = os.path.join(self.tmp_dir.name, 'casmvs_inp_dir')
        casmvs_res_dir = os.path.join(self.tmp_dir.name, 'casmvs_res_dir')
        os.makedirs(casmvs_inp_dir, exist_ok=True)
        os.makedirs(casmvs_res_dir, exist_ok=True)

        input_dict = {
            'input_dir': input,
            'casmvs_inp_dir': casmvs_inp_dir,
            'casmvs_res_dir': casmvs_res_dir
        }

        self.model.preprocess_make_pair(input_dict)

        return input_dict

    def forward(self, input: Dict[str, Any]) -> Dict[str, Any]:
        results = self.model.forward(input)
        return results

    def postprocess(self, inputs: Dict[str, Any]) -> Dict[str, Any]:

        pcd = self.model.postprocess(inputs)

        # clear tmp dir
        if self.tmp_dir is not None:
            self.tmp_dir.cleanup()

        outputs = {
            OutputKeys.OUTPUT: pcd,
        }

        return outputs
