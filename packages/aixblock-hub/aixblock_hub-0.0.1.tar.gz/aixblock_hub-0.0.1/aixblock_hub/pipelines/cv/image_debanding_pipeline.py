# Copyright (c) AIxBlock, Inc. 
from typing import Any, Dict, Optional, Union

import torch
from torchvision import transforms

from aixblock_hub.metainfo import Pipelines
from aixblock_hub.models.base import Model
from aixblock_hub.models.cv.image_debanding import RRDBImageDebanding
from aixblock_hub.outputs import OutputKeys
from aixblock_hub.pipelines.base import Input, Pipeline
from aixblock_hub.pipelines.builder import PIPELINES
from aixblock_hub.preprocessors import LoadImage
from aixblock_hub.utils.constant import Tasks
from aixblock_hub.utils.logger import get_logger

logger = get_logger()


@PIPELINES.register_module(
    Tasks.image_debanding, module_name=Pipelines.image_debanding)
class ImageDebandingPipeline(Pipeline):

    def __init__(self, model: Union[RRDBImageDebanding, str], **kwargs):
        """The inference pipeline for image debanding.

        Args:
            model (`str` or `Model` or module instance): A model instance or a model local dir
                or a model id in the model hub.
            preprocessor (`Preprocessor`, `optional`): A Preprocessor instance.
            kwargs (dict, `optional`):
                Extra kwargs passed into the preprocessor's constructor.

        Example:
            >>> import cv2
            >>> from aixblock_hub.outputs import OutputKeys
            >>> from aixblock_hub.pipelines import pipeline
            >>> from aixblock_hub.utils.constant import Tasks
            >>> debanding = pipeline(Tasks.image_debanding, model='damo/cv_rrdb_image-debanding')
                result = debanding(
                    'https://app.aixblock.io/test/images/debanding.png')
            >>> cv2.imwrite('result.png', result[OutputKeys.OUTPUT_IMG])
        """
        super().__init__(model=model, **kwargs)
        self.model.eval()

        if torch.cuda.is_available():
            self._device = torch.device('cuda')
        else:
            self._device = torch.device('cpu')

    def preprocess(self, input: Input) -> Dict[str, Any]:
        img = LoadImage.convert_to_img(input)
        test_transforms = transforms.Compose([transforms.ToTensor()])
        img = test_transforms(img)
        result = {'src': img.unsqueeze(0).to(self._device)}
        return result

    @torch.no_grad()
    def forward(self, input: Dict[str, Any]) -> Dict[str, Any]:
        return super().forward(input)

    def postprocess(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        output_img = (inputs['outputs'].squeeze(0) * 255.).type(
            torch.uint8).cpu().permute(1, 2, 0).numpy()[:, :, ::-1]
        return {OutputKeys.OUTPUT_IMG: output_img}
