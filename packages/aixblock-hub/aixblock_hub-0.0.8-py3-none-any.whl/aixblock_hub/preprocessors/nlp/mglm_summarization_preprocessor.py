# Copyright (c) 2022 Zhipu.AI

import os.path as osp
import re
from typing import Any, Dict, Iterable, Optional, Tuple, Union

from aixblock_hub.metainfo import Models, Preprocessors
from aixblock_hub.outputs import OutputKeys
from aixblock_hub.preprocessors.base import Preprocessor
from aixblock_hub.preprocessors.builder import PREPROCESSORS
from aixblock_hub.utils.config import Config, ConfigFields
from aixblock_hub.utils.constant import Fields, InputFields, ModeKeys, ModelFile
from aixblock_hub.utils.hub import get_model_type, parse_label_mapping
from aixblock_hub.utils.logger import get_logger
from aixblock_hub.utils.nlp import import_external_nltk_data
from aixblock_hub.utils.type_assert import type_assert


@PREPROCESSORS.register_module(
    Fields.nlp, module_name=Preprocessors.mglm_summarization)
class MGLMSummarizationPreprocessor(Preprocessor):

    def __init__(self, *args, **kwargs):
        """preprocess the data
        Args:
            model_dir (str): model path
        """
        super().__init__(*args, **kwargs)

    @type_assert(object, (str, tuple, Dict))
    def __call__(self, data: Union[str, tuple, Dict]) -> Dict[str, Any]:
        return data
