# Copyright (c) AIxBlock, Inc. 

import os
from typing import Any, Dict

import json
import wenetruntime as wenet

from aixblock_hub.metainfo import Models
from aixblock_hub.models.base import Model
from aixblock_hub.models.builder import MODELS
from aixblock_hub.utils.constant import Tasks

__all__ = ['WeNetAutomaticSpeechRecognition']


@MODELS.register_module(
    Tasks.auto_speech_recognition, module_name=Models.wenet_asr)
class WeNetAutomaticSpeechRecognition(Model):

    def __init__(self, model_dir: str, am_model_name: str,
                 model_config: Dict[str, Any], *args, **kwargs):
        """initialize the info of model.

        Args:
            model_dir (str): the model path.
        """
        super().__init__(model_dir, am_model_name, model_config, *args,
                         **kwargs)
        self.decoder = wenet.Decoder(model_dir, lang='chs')

    def forward(self, inputs: Dict[str, Any]) -> str:
        if inputs['audio_format'] == 'wav':
            rst = self.decoder.decode_wav(inputs['audio'])
        else:
            rst = self.decoder.decode(inputs['audio'])
        text = json.loads(rst)['nbest'][0]['sentence']
        return {'text': text}
