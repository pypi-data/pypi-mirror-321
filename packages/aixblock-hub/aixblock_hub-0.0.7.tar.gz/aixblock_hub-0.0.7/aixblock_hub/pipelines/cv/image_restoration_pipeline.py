# Copyright (c) AIxBlock, Inc. 

from typing import Any, Dict

from aixblock_hub.metainfo import Pipelines
from aixblock_hub.outputs import OutputKeys
from aixblock_hub.pipelines.base import Input, Pipeline
from aixblock_hub.pipelines.builder import PIPELINES
from aixblock_hub.preprocessors import LoadImage
from aixblock_hub.utils.constant import Tasks


@PIPELINES.register_module(
    Tasks.image_demoireing, module_name=Pipelines.image_demoire)
class ImageRestorationPipeline(Pipeline):
    """ Image Restoration Pipeline .

    Take image_demoireing as an example:
        >>> from aixblock_hub.pipelines import pipeline
        >>> image_demoire = pipeline(Tasks.image_demoireing, model=model_id)
        >>> image_demoire("https://app.aixblock.io/test/images/image_moire.jpg")

    """

    def __init__(self, model: str, **kwargs):
        """
            model: model id on aixblock hub.
        """
        super().__init__(model=model, auto_collate=False, **kwargs)

    def preprocess(self, input: Input) -> Dict[str, Any]:

        img = LoadImage.convert_to_ndarray(input)
        img_h, img_w, _ = img.shape
        result = self.preprocessor(img)
        result['img_h'] = img_h
        result['img_w'] = img_w
        return result

    def forward(self, input: Dict[str, Any]) -> Dict[str, Any]:

        output = self.model(input)
        result = {
            'img': output,
            'img_w': input['img_w'],
            'img_h': input['img_h']
        }
        return result

    def postprocess(self, inputs: Dict[str, Any]) -> Dict[str, Any]:

        data = inputs['img']
        outputs = {OutputKeys.OUTPUT_IMG: data}
        return outputs
