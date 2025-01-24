# Copyright (c) AIxBlock, Inc. 

from typing import Any, Dict, Union

from transformers import AutoTokenizer

from aixblock_hub.preprocessors.base import Preprocessor
from aixblock_hub.preprocessors.builder import PREPROCESSORS
from aixblock_hub.utils.constant import Fields, InputFields


@PREPROCESSORS.register_module(Fields.nlp)
class Tokenize(Preprocessor):

    def __init__(self, tokenizer_name) -> None:
        self.tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)

    def __call__(self, data: Union[str, Dict[str, Any]]) -> Dict[str, Any]:
        if isinstance(data, str):
            data = {InputFields.text: data}
        token_dict = self.tokenizer(data[InputFields.text])
        data.update(token_dict)
        return data
