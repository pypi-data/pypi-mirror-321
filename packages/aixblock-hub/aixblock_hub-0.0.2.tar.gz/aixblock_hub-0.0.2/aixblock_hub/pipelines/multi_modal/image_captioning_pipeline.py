# Copyright (c) AIxBlock, Inc. 
from typing import Any, Dict, Optional, Union

import numpy as np
import torch

from aixblock_hub.metainfo import Pipelines
from aixblock_hub.models.multi_modal import (CLIP_Interrogator, MPlugForAllTasks,
                                           OfaForAllTasks)
from aixblock_hub.pipelines.base import Model, Pipeline
from aixblock_hub.pipelines.builder import PIPELINES
from aixblock_hub.pipelines.util import batch_process
from aixblock_hub.preprocessors import (
    ImageCaptioningClipInterrogatorPreprocessor, MPlugPreprocessor,
    OfaPreprocessor, Preprocessor, load_image)
from aixblock_hub.utils.constant import ModelFile, Tasks
from aixblock_hub.utils.logger import get_logger

logger = get_logger()


@PIPELINES.register_module(
    Tasks.image_captioning, module_name=Pipelines.image_captioning)
class ImageCaptioningPipeline(Pipeline):

    def __init__(self,
                 model: Union[Model, str],
                 preprocessor: Optional[Preprocessor] = None,
                 **kwargs):
        """
        use `model` and `preprocessor` to create a image captioning pipeline for prediction
        Args:
            model: model id on aixblock hub.
        Examples:
        from aixblock_hub.pipelines import pipeline
        from aixblock_hub.utils.constant import Tasks

        model_id = 'damo/cv_clip-interrogator'
        input_image = "test.png"

        pipeline_ci = pipeline(Tasks.image_captioning, model=model_id)
        print(pipeline_ci(input_image))


        """
        super().__init__(model=model, preprocessor=preprocessor, **kwargs)
        self.model.eval()
        assert isinstance(self.model, Model), \
            f'please check whether model config exists in {ModelFile.CONFIGURATION}'
        if preprocessor is None:

            if isinstance(self.model, OfaForAllTasks):
                self.preprocessor = OfaPreprocessor(self.model.model_dir)
            elif isinstance(self.model, MPlugForAllTasks):
                self.preprocessor = MPlugPreprocessor(self.model.model_dir)
            elif isinstance(self.model, CLIP_Interrogator):
                self.preprocessor = ImageCaptioningClipInterrogatorPreprocessor(
                )

    def _batch(self, data):
        if isinstance(self.model, OfaForAllTasks):
            return batch_process(self.model, data)
        elif isinstance(self.model, MPlugForAllTasks):
            from transformers.tokenization_utils_base import BatchEncoding
            batch_data = dict(train=data[0]['train'])
            batch_data['image'] = torch.cat([d['image'] for d in data])
            question = {}
            for k in data[0]['question'].keys():
                question[k] = torch.cat([d['question'][k] for d in data])
            batch_data['question'] = BatchEncoding(question)
            return batch_data
        else:
            return super(ImageCaptioningPipeline, self)._batch(data)

    def forward(self, inputs: Dict[str, Any],
                **forward_params) -> Dict[str, Any]:
        with torch.no_grad():
            return super().forward(inputs, **forward_params)

    def postprocess(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        return inputs
