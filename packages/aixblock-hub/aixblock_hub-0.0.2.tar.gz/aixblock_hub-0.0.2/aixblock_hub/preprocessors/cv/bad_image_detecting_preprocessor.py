# Copyright (c) AIxBlock, Inc. 
import math
from typing import Any, Dict

import torch
import torch.nn.functional as F
from numpy import ndarray
from PIL import Image
from torchvision import transforms

from aixblock_hub.metainfo import Preprocessors
from aixblock_hub.preprocessors.base import Preprocessor
from aixblock_hub.preprocessors.builder import PREPROCESSORS
from aixblock_hub.utils.constant import Fields
from aixblock_hub.utils.type_assert import type_assert


@PREPROCESSORS.register_module(
    Fields.cv, module_name=Preprocessors.bad_image_detecting_preprocessor)
class BadImageDetectingPreprocessor(Preprocessor):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.transform_input = transforms.Compose([
            transforms.Resize(224),
            transforms.CenterCrop(224),
            transforms.ToTensor()
        ])

    @type_assert(object, object)
    def __call__(self, data: ndarray) -> Dict[str, Any]:
        image = Image.fromarray(data)
        data = self.transform_input(image)
        data = data.unsqueeze(0)
        return {'input': data.float()}
