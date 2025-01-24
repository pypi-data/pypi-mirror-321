# Copyright (c) AIxBlock, Inc. 

import os
from typing import Any, Dict, Generator, List, Union

from aixblock_hub.pipelines.base import Input, Pipeline
from aixblock_hub.utils.constant import Hubs
from aixblock_hub.utils.device import create_device
from aixblock_hub.utils.hub import snapshot_download


class DiffusersPipeline(Pipeline):

    def __init__(self, model: str, device: str = 'gpu', **kwargs):
        """
        use `model` to create a diffusers pipeline
        Args:
            model: model id on aixblock hub or local dir.
            device: str = 'gpu'
        """

        self.device_name = device
        self.cfg = None
        self.preprocessor = None
        self.framework = None
        self.device = create_device(self.device_name)
        self.hubs = kwargs.get('hubs', Hubs.aixblock)

        # make sure we download the model from aixblock hub
        model_folder = model
        if not os.path.isdir(model_folder):
            if self.hubs != Hubs.aixblock:
                raise NotImplementedError(
                    'Only support model retrieval from aixblock hub for now.'
                )
            model_folder = snapshot_download(model)

        self.model = model_folder
        self.models = [self.model]
        self.has_multiple_models = len(self.models) > 1

    def preprocess(self, inputs: Dict[str, Any], **kwargs) -> Dict[str, Any]:
        return inputs

    def postprocess(self, inputs: Dict[str, Any], **kwargs) -> Dict[str, Any]:
        return inputs

    def __call__(self, input: Union[Input, List[Input]], *args,
                 **kwargs) -> Union[Dict[str, Any], Generator]:
        preprocess_params, forward_params, postprocess_params = self._sanitize_parameters(
            **kwargs)
        self._check_input(input)
        out = self.preprocess(input, **preprocess_params)
        out = self.forward(out, **forward_params)
        out = self.postprocess(out, **postprocess_params)
        self._check_output(out)
        return out
