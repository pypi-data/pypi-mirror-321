# Copyright (c) AIxBlock, Inc. 

from aixblock_hub.metainfo import Heads, Models
from aixblock_hub.models.builder import MODELS
from aixblock_hub.models.nlp.task_models.fill_mask import ModelForFillMask
from aixblock_hub.utils import logger as logging
from aixblock_hub.utils.constant import Tasks

logger = logging.get_logger()


@MODELS.register_module(Tasks.fill_mask, module_name=Models.bert)
class BertForMaskedLM(ModelForFillMask):

    base_model_type = Models.bert
    head_type = Heads.bert_mlm
