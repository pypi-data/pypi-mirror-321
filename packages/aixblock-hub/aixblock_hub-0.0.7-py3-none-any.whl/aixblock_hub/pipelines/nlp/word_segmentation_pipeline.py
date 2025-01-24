# Copyright (c) AIxBlock, Inc. 

from typing import Any, Dict, Optional, Union

import torch

from aixblock_hub.metainfo import Pipelines
from aixblock_hub.models import Model
from aixblock_hub.outputs import OutputKeys
from aixblock_hub.pipelines.base import Pipeline
from aixblock_hub.pipelines.builder import PIPELINES
from aixblock_hub.pipelines.nlp import TokenClassificationPipeline
from aixblock_hub.preprocessors import (
    Preprocessor, TokenClassificationTransformersPreprocessor,
    WordSegmentationPreprocessorThai)
from aixblock_hub.utils.constant import ModelFile, Tasks
from aixblock_hub.utils.tensor_utils import (torch_nested_detach,
                                           torch_nested_numpify)

__all__ = ['WordSegmentationPipeline', 'WordSegmentationThaiPipeline']


@PIPELINES.register_module(
    Tasks.word_segmentation, module_name=Pipelines.word_segmentation)
class WordSegmentationPipeline(TokenClassificationPipeline):
    """Use `model` and `preprocessor` to create a nlp word segment pipeline for prediction.

    NOTE: The preprocessor will first split the sentence into single characters,
    then feed them into the tokenizer with the parameter is_split_into_words=True.

    Examples:
        >>> from aixblock_hub.pipelines import pipeline
        >>> pipeline_ins = pipeline(task='word-segmentation',
        >>>    model='damo/nlp_structbert_word-segmentation_chinese-base')
        >>> sentence1 = '今天天气不错，适合出去游玩'
        >>> print(pipeline_ins(sentence1))

    To view other examples plese check tests/pipelines/test_word_segmentation.py.
    """

    def postprocess(self,
                    inputs: Dict[str, Any],
                    output_final_sentence=True,
                    **postprocess_params) -> Dict[str, Any]:
        """Process the prediction results

        Args:
            inputs (Dict[str, Any]): should be tensors from model
            output_final_sentence (bool): Output the cut sentence splitted by blanks or not.
                If False, the pipeline will output the original token-label information.

        Returns:
            Dict[str, Any]: The prediction results.
        """
        chunks = self._chunk_process(inputs, **postprocess_params)

        # for cws outputs
        if output_final_sentence:
            spans = [
                chunk['span'] for chunk in chunks if chunk['span'].strip()
            ]
            seg_result = [span for span in spans]
            outputs = {OutputKeys.OUTPUT: seg_result}

        # for ner outputs
        else:
            outputs = {OutputKeys.OUTPUT: chunks}
        return outputs


@PIPELINES.register_module(
    Tasks.word_segmentation,
    module_name=Pipelines.multilingual_word_segmentation)
class MultilingualWordSegmentationPipeline(WordSegmentationPipeline):

    def postprocess(self,
                    inputs: Dict[str, Any],
                    output_final_sentence=True,
                    **postprocess_params) -> Dict[str, Any]:
        chunks = self._chunk_process(inputs, **postprocess_params)
        word_segments = [entity['span'] for entity in chunks]
        return {OutputKeys.OUTPUT: word_segments}


@PIPELINES.register_module(
    Tasks.word_segmentation, module_name=Pipelines.word_segmentation_thai)
class WordSegmentationThaiPipeline(MultilingualWordSegmentationPipeline):

    def __init__(self,
                 model: Union[Model, str],
                 preprocessor: Optional[Preprocessor] = None,
                 config_file: str = None,
                 device: str = 'gpu',
                 auto_collate=True,
                 sequence_length=512,
                 **kwargs):
        super().__init__(
            model=model,
            preprocessor=preprocessor,
            config_file=config_file,
            device=device,
            auto_collate=auto_collate)

        assert isinstance(self.model, Model), \
            f'please check whether model config exists in {ModelFile.CONFIGURATION}'

        if preprocessor is None:
            self.preprocessor = WordSegmentationPreprocessorThai(
                self.model.model_dir,
                sequence_length=sequence_length,
                **kwargs)

    def postprocess(self, inputs: Dict[str, Any],
                    **postprocess_params) -> Dict[str, str]:
        chunks = self._chunk_process(inputs, **postprocess_params)
        word_segments = [entity['span'].replace(' ', '') for entity in chunks]
        return {OutputKeys.OUTPUT: word_segments}
