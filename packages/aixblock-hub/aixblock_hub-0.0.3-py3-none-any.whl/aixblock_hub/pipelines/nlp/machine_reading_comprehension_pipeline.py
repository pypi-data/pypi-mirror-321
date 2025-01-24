from typing import Any, Dict, Union

import torch

from aixblock_hub.metainfo import Pipelines, Preprocessors
from aixblock_hub.models.base import Model
from aixblock_hub.outputs import MachineReadingComprehensionOutput, OutputKeys
from aixblock_hub.pipelines.base import Pipeline
from aixblock_hub.pipelines.builder import PIPELINES
from aixblock_hub.preprocessors import Preprocessor
from aixblock_hub.utils.constant import Fields, Tasks


@PIPELINES.register_module(
    Tasks.machine_reading_comprehension,
    module_name=Pipelines.machine_reading_comprehension_for_ner)
class MachineReadingComprehensionForNERPipeline(Pipeline):
    '''
    Pipeline for Pretrained Machine Reader (PMR) finetuned on Named Entity Recognition (NER)

    Examples:

    >>> from aixblock_hub.pipelines import pipeline
    >>> pipeline_ins = pipeline(
    >>>        task=Tasks.machine_reading_comprehension,
    >>>        model='damo/nlp_roberta_machine-reading-comprehension_for-ner')
    >>> pipeline_ins('Soccer - Japan get lucky win , China in surprise defeat .')
    >>> {'ORG': [], 'PER': [], 'LOC': [' Japan', ' China'], 'MISC': []}
    '''

    def __init__(self,
                 model: Union[Model, str],
                 preprocessor: Preprocessor = None,
                 config_file: str = None,
                 device: str = 'gpu',
                 auto_collate=True,
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
            self.preprocessor = Preprocessor.from_pretrained(
                self.model.model_dir, **kwargs)
        self.labels = [label for label in self.preprocessor.label2query]

        self.model.eval()

    def forward(
        self, inputs, **forward_params
    ) -> Union[Dict[str, Any], MachineReadingComprehensionOutput]:
        with torch.no_grad():
            outputs = self.model(**inputs)
        span_logits = outputs['span_logits']

        return MachineReadingComprehensionOutput(
            span_logits=span_logits,
            input_ids=inputs['input_ids'],
        )

    def postprocess(
        self, inputs: Union[Dict[str, Any], MachineReadingComprehensionOutput]
    ) -> Dict[str, Any]:

        span_preds = inputs['span_logits'] > 0
        extracted_indices = torch.nonzero(span_preds.long())

        result = {label: [] for label in self.labels}
        for index in extracted_indices:
            label = self.labels[index[0]]
            start = index[1]
            end = index[2] + 1
            ids = inputs['input_ids'][index[0], start:end]
            entity = self.preprocessor.tokenizer.decode(ids)
            result[label].append(entity)

        return result
