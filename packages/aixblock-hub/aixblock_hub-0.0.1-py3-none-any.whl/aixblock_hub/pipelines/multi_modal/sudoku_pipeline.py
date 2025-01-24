# Copyright (c) AIxBlock, Inc. 
from typing import Any, Dict, Optional, Union

import torch

from aixblock_hub.metainfo import Pipelines
from aixblock_hub.models.multi_modal import OfaForAllTasks
from aixblock_hub.pipelines.base import Model, Pipeline
from aixblock_hub.pipelines.builder import PIPELINES
from aixblock_hub.pipelines.util import batch_process
from aixblock_hub.preprocessors import OfaPreprocessor, Preprocessor
from aixblock_hub.utils.constant import Tasks
from aixblock_hub.utils.logger import get_logger

logger = get_logger()


@PIPELINES.register_module(Tasks.sudoku, module_name=Pipelines.ofa_sudoku)
class SudokuPipeline(Pipeline):
    R"""
    pipeline for sudoku solving
    """

    def __init__(self,
                 model: Union[Model, str],
                 preprocessor: Optional[Preprocessor] = None,
                 **kwargs):
        """
        use `model` and `preprocessor` to create a pipeline for solving sudoku
        Args:
            model: model id on aixblock hub.
        """
        super().__init__(model=model, preprocessor=preprocessor, **kwargs)
        self.model.eval()
        if preprocessor is None:
            if isinstance(self.model, OfaForAllTasks):
                self.preprocessor = OfaPreprocessor(self.model.model_dir)
            else:
                raise 'no preprocessor is provided'

    def _batch(self, data):
        if isinstance(self.model, OfaForAllTasks):
            return batch_process(self.model, data)
        else:
            return super(SudokuPipeline, self)._batch(data)

    def forward(self, inputs: Dict[str, Any],
                **forward_params) -> Dict[str, Any]:
        with torch.no_grad():
            return super().forward(inputs, **forward_params)

    def postprocess(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        return inputs
