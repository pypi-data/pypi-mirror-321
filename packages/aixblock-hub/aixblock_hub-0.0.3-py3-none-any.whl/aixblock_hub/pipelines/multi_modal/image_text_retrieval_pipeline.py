# Copyright (c) AIxBlock, Inc. 
from typing import Any, Dict, Optional, Union

import torch

from aixblock_hub.metainfo import Pipelines
from aixblock_hub.outputs import OutputKeys
from aixblock_hub.pipelines.base import Model, Pipeline
from aixblock_hub.pipelines.builder import PIPELINES
from aixblock_hub.preprocessors import MPlugPreprocessor, Preprocessor
from aixblock_hub.utils.constant import ModelFile, Tasks
from aixblock_hub.utils.logger import get_logger

logger = get_logger()


@PIPELINES.register_module(
    Tasks.image_text_retrieval, module_name=Pipelines.image_text_retrieval)
class ImageTextRetrievalPipeline(Pipeline):

    def __init__(self,
                 model: Union[Model, str],
                 preprocessor: Optional[Preprocessor] = None,
                 **kwargs):
        """
        use `model` and `preprocessor` to create a
        image text retrieval pipeline for prediction
        Args:
            model: model id on aixblock hub.
        """
        super().__init__(model=model, preprocessor=preprocessor, **kwargs)
        self.model.eval()
        assert isinstance(self.model, Model), \
            f'please check whether model config exists in {ModelFile.CONFIGURATION}'
        if preprocessor is None:
            self.preprocessor = MPlugPreprocessor(self.model.model_dir)

    def forward(self, inputs: Dict[str, Any],
                **forward_params) -> Dict[str, Any]:
        with torch.no_grad():
            return super().forward(inputs, **forward_params)

    def postprocess(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        return inputs
