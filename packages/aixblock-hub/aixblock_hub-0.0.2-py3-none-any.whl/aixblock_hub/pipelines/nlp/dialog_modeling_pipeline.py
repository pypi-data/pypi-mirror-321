# Copyright (c) AIxBlock, Inc. 

from typing import Dict, Union

from aixblock_hub.metainfo import Pipelines
from aixblock_hub.models import Model
from aixblock_hub.models.nlp import SpaceForDialogModeling
from aixblock_hub.outputs import OutputKeys
from aixblock_hub.pipelines.base import Pipeline, Tensor
from aixblock_hub.pipelines.builder import PIPELINES
from aixblock_hub.preprocessors import DialogModelingPreprocessor
from aixblock_hub.utils.constant import Tasks

__all__ = ['DialogModelingPipeline']


@PIPELINES.register_module(
    Tasks.task_oriented_conversation, module_name=Pipelines.dialog_modeling)
class DialogModelingPipeline(Pipeline):

    def __init__(self,
                 model: Union[SpaceForDialogModeling, str],
                 preprocessor: DialogModelingPreprocessor = None,
                 config_file: str = None,
                 device: str = 'gpu',
                 auto_collate=True,
                 **kwargs):
        """Use `model` and `preprocessor` to create a dialog modeling pipeline for dialog response generation

        Args:
            model (str or SpaceForDialogModeling): Supply either a local model dir or a model id from the model hub,
            or a SpaceForDialogModeling instance.
            preprocessor (DialogModelingPreprocessor): An optional preprocessor instance.
            kwargs (dict, `optional`):
                Extra kwargs passed into the preprocessor's constructor.
        """
        super().__init__(
            model=model,
            preprocessor=preprocessor,
            config_file=config_file,
            device=device,
            auto_collate=auto_collate)
        if preprocessor is None:
            self.preprocessor = DialogModelingPreprocessor(
                self.model.model_dir, **kwargs)

    def postprocess(self, inputs: Dict[str, Tensor]) -> Dict[str, str]:
        """process the prediction results

        Args:
            inputs (Dict[str, Any]): _description_

        Returns:
            Dict[str, str]: the prediction results
        """
        sys_rsp = self.preprocessor.text_field.tokenizer.convert_ids_to_tokens(
            inputs['resp'])
        assert len(sys_rsp) > 2
        sys_rsp = sys_rsp[1:len(sys_rsp) - 1]
        inputs[OutputKeys.OUTPUT] = sys_rsp

        return inputs
