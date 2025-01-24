# Copyright (c) AIxBlock, Inc. 

import os
from typing import Any, Dict

import json

from aixblock_hub.metainfo import Preprocessors
from aixblock_hub.preprocessors.base import Preprocessor
from aixblock_hub.preprocessors.builder import PREPROCESSORS
from aixblock_hub.preprocessors.nlp import IntentBPETextField
from aixblock_hub.utils.config import Config
from aixblock_hub.utils.constant import Fields, ModelFile
from aixblock_hub.utils.type_assert import type_assert

__all__ = ['DialogIntentPredictionPreprocessor']


@PREPROCESSORS.register_module(
    Fields.nlp, module_name=Preprocessors.dialog_intent_preprocessor)
class DialogIntentPredictionPreprocessor(Preprocessor):

    def __init__(self, model_dir: str, *args, **kwargs):
        """preprocess the data

        Args:
            model_dir (str): model path
        """
        super().__init__(*args, **kwargs)

        self.model_dir: str = model_dir
        self.config = Config.from_file(
            os.path.join(self.model_dir, ModelFile.CONFIGURATION))
        self.text_field = IntentBPETextField(
            self.model_dir, config=self.config)

        self.categories = None
        with open(
                os.path.join(self.model_dir, 'categories.json'),
                'r',
                encoding='utf-8') as f:
            self.categories = json.load(f)
        assert len(self.categories) == 77

    @type_assert(object, str)
    def __call__(self, data: str) -> Dict[str, Any]:
        """process the raw input data

        Args:
            data (str): a sentence
                Example:
                    'What do I need to do for the card activation?'

        Returns:
            Dict[str, Any]: the preprocessed data
                Example:
                    {
                        'src_token': array([[13,  2054,  2079,  1045...]]),
                        'src_pos': array([[ 0,  1,  2,  3...]]),
                        'src_type': array([[1, 1, 1, 1...]]),
                        'src_turn': array([[1, 1, 1, 1...]]),
                        'src_mask': array([[1, 1, 1, 1...]]),
                        'mlm_token': array([[13,  2054,  2079,  1045...]]),
                        'mlm_label': array([[0, 0, 0, 0...]]),
                        'mlm_mask': array([[0, 0, 0, 0...]]),
                        'tgt_token': array([[29, 30, 31, 32...]]),
                        'tgt_mask': array([[1, 1, 1, 1...]]),
                        'ids': array([0]),
                        'intent_label': array([-1])
                    }
        """
        samples = self.text_field.preprocessor([data])
        samples, _ = self.text_field.collate_fn_multi_turn(samples)

        return samples
