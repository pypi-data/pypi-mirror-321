# Copyright (c) AIxBlock, Inc. 
from typing import TYPE_CHECKING

from aixblock_hub.utils.import_utils import LazyImportModule

if TYPE_CHECKING:
    from .generic_automatic_speech_recognition import GenericAutomaticSpeechRecognition

else:
    _import_structure = {
        'generic_automatic_speech_recognition':
        ['GenericAutomaticSpeechRecognition'],
    }

    import sys

    sys.modules[__name__] = LazyImportModule(
        __name__,
        globals()['__file__'],
        _import_structure,
        module_spec=__spec__,
        extra_objects={},
    )
