# Copyright (c) AIxBlock, Inc. 
from typing import TYPE_CHECKING

from aixblock_hub.trainers.utils.log_buffer import LogBuffer
from aixblock_hub.utils.import_utils import LazyImportModule

if TYPE_CHECKING:
    from .base import LoggerHook
    from .tensorboard_hook import TensorboardHook
    from .text_logger_hook import TextLoggerHook
else:
    _import_structure = {
        'base': ['LoggerHook'],
        'tensorboard_hook': ['TensorboardHook'],
        'text_logger_hook': ['TextLoggerHook']
    }
    import sys
    sys.modules[__name__] = LazyImportModule(
        __name__,
        globals()['__file__'],
        _import_structure,
        module_spec=__spec__,
        extra_objects={},
    )
