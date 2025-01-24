# Copyright (c) AIxBlock, Inc. 
from typing import TYPE_CHECKING

from aixblock_hub.utils.import_utils import LazyImportModule

if TYPE_CHECKING:
    from .ecapa_tdnn import SpeakerVerificationECAPATDNN

else:
    _import_structure = {'ecapa_tdnn': ['SpeakerVerificationECAPATDNN']}
    import sys
    sys.modules[__name__] = LazyImportModule(
        __name__,
        globals()['__file__'],
        _import_structure,
        module_spec=__spec__,
        extra_objects={},
    )
