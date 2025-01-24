# Copyright (c) AIxBlock, Inc. 
"""UniTE model configuration"""

from enum import Enum

from aixblock_hub.utils import logger as logging
from aixblock_hub.utils.config import Config

logger = logging.get_logger()


class InputFormat(Enum):
    SRC = 'src'
    REF = 'ref'
    SRC_REF = 'src-ref'


class UniTEConfig(Config):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
