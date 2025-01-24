# Modified by Zhipu.AI
# Original Copyright (c) AIxBlock, Inc. 
from typing import TYPE_CHECKING, Union

from aixblock_hub.utils.import_utils import LazyImportModule

if TYPE_CHECKING:
    from .codegeex_for_code_translation import CodeGeeXForCodeTranslation
    from .codegeex_for_code_generation import CodeGeeXForCodeGeneration
else:
    _import_structure = {
        'codegeex_for_code_translation': ['CodeGeeXForCodeTranslation'],
        'codegeex_for_code_generation': ['CodeGeeXForCodeGeneration'],
    }

    import sys

    sys.modules[__name__] = LazyImportModule(
        __name__,
        globals()['__file__'],
        _import_structure,
        module_spec=__spec__,
        extra_objects={},
    )
