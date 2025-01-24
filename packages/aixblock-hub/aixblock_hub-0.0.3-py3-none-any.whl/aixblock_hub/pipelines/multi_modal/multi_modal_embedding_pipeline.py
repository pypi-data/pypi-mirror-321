# Copyright (c) AIxBlock, Inc. 

from typing import Any, Dict, Optional, Union

from aixblock_hub.metainfo import Pipelines
from aixblock_hub.models.multi_modal.clip.model import CLIPForMultiModalEmbedding
from aixblock_hub.pipelines.base import Input, Model, Pipeline
from aixblock_hub.pipelines.builder import PIPELINES
from aixblock_hub.preprocessors.multi_modal import CLIPPreprocessor, Preprocessor
from aixblock_hub.utils.constant import Tasks
from aixblock_hub.utils.logger import get_logger

logger = get_logger()


@PIPELINES.register_module(
    Tasks.image_text_retrieval, module_name=Pipelines.multi_modal_embedding)
@PIPELINES.register_module(
    Tasks.multi_modal_embedding, module_name=Pipelines.multi_modal_embedding)
class MultiModalEmbeddingPipeline(Pipeline):

    def __init__(self,
                 model: Union[Model, str],
                 preprocessor: Optional[Preprocessor] = None,
                 **kwargs):
        """
        use `model` and `preprocessor` to create a kws pipeline for prediction
        Args:
            model: model id on aixblock hub.
        """
        super().__init__(model=model, preprocessor=preprocessor, **kwargs)
        self.model.eval()
        if preprocessor is None:
            if isinstance(self.model, CLIPForMultiModalEmbedding):
                self.preprocessor = CLIPPreprocessor(self.model.model_dir)
            else:
                raise NotImplementedError

    def forward(self, input: Dict[str, Any]) -> Dict[str, Any]:
        return self.model(self.preprocess(input))

    def postprocess(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        return inputs
