# Copyright (c) AIxBlock, Inc. 

from typing import Any, Dict, Tuple, Union

import torch

from aixblock_hub.metainfo import Preprocessors
from aixblock_hub.outputs import OutputKeys
from aixblock_hub.preprocessors.builder import PREPROCESSORS
from aixblock_hub.utils.constant import Fields, ModeKeys
from aixblock_hub.utils.type_assert import type_assert
from .token_classification_preprocessor import \
    TokenClassificationTransformersPreprocessor


@PREPROCESSORS.register_module(
    Fields.nlp, module_name=Preprocessors.viet_ner_tokenizer)
class NERPreprocessorViet(TokenClassificationTransformersPreprocessor):

    @type_assert(object, (str, dict))
    def __call__(self, data: Union[Dict, str]) -> Dict[str, Any]:
        from pyvi import ViTokenizer
        if isinstance(data, str):
            text = data
        else:
            text = data[self.first_sequence]
        seg_words = [
            t.strip(' ') for t in ViTokenizer.tokenize(text).split(' ')
            if t.strip(' ') != ''
        ]
        raw_words = []
        for w in seg_words:
            raw_words.extend(w.split('_'))
        segmented_data = ' '.join(raw_words)
        output = super().__call__(segmented_data)

        return output
