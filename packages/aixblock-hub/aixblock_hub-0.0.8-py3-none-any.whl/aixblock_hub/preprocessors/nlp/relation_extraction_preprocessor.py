# Copyright (c) AIxBlock, Inc. 

from typing import Any, Dict

from transformers import AutoTokenizer

from aixblock_hub.metainfo import Preprocessors
from aixblock_hub.preprocessors import Preprocessor
from aixblock_hub.preprocessors.builder import PREPROCESSORS
from aixblock_hub.utils.constant import Fields, ModeKeys
from aixblock_hub.utils.type_assert import type_assert


@PREPROCESSORS.register_module(
    Fields.nlp, module_name=Preprocessors.re_tokenizer)
class RelationExtractionTransformersPreprocessor(Preprocessor):

    def __init__(
        self,
        model_dir: str,
        mode: str = ModeKeys.INFERENCE,
        **kwargs,
    ):
        """The preprocessor for relation Extraction task, based on transformers' tokenizer.

        Args:
            model_dir: The model dir used to initialize the tokenizer.
            mode: The mode for the preprocessor.
        """

        super().__init__(mode)
        self.model_dir: str = model_dir
        self.tokenizer = AutoTokenizer.from_pretrained(
            model_dir, use_fast=True)

    @type_assert(object, str)
    def __call__(self, data: str, **kwargs) -> Dict[str, Any]:
        """process the raw input data

        Args:
            data (str): a sentence
                Example:
                    'you are so handsome.'

        Returns:
            Dict[str, Any]: the preprocessed data
        """

        # preprocess the data for the model input
        text = data
        if 'return_tensors' not in kwargs:
            kwargs['return_tensors'] = 'pt'
        output = self.tokenizer([text], **kwargs)
        return {
            'text': text,
            'input_ids': output['input_ids'],
            'attention_mask': output['attention_mask'],
            'offsets': output[0].offsets
        }
