# Copyright (c) AIxBlock, Inc. 

from typing import Any, Dict, Union

from transformers import AutoTokenizer

from aixblock_hub.metainfo import Preprocessors
from aixblock_hub.preprocessors import Preprocessor
from aixblock_hub.preprocessors.builder import PREPROCESSORS
from aixblock_hub.utils.constant import Fields, ModeKeys
from aixblock_hub.utils.hub import get_model_type
from .transformers_tokenizer import NLPTokenizer


@PREPROCESSORS.register_module(
    Fields.nlp, module_name=Preprocessors.siamese_uie_preprocessor)
class SiameseUiePreprocessor(Preprocessor):
    """The tokenizer preprocessor used in zero shot classification.
    """

    def __init__(
        self,
        model_dir: str,
        mode: str = ModeKeys.INFERENCE,
        **kwargs,
    ):
        """preprocess the data
        Args:
            model_dir (str): model path
        """
        super().__init__(mode)
        self.model_dir: str = model_dir
        self.tokenizer = AutoTokenizer.from_pretrained(
            model_dir, use_fast=True)

    def __call__(self, data: list, **kwargs) -> Dict[str, Any]:
        """process the raw input data

        Args:
            data (str or dict): a sentence
                Example:
                    'you are so handsome.'

        Returns:
            Dict[str, Any]: the preprocessed data
        """
        features = self.tokenizer(data, **kwargs)
        return features
