# Copyright (c) AIxBlock, Inc. 
from typing import TYPE_CHECKING

from aixblock_hub.utils.import_utils import LazyImportModule

if TYPE_CHECKING:

    from .hrnet_v2 import PoseHighResolutionNetV2

else:
    _import_structure = {
        'hrnet_v2': ['PoseHighResolutionNetV2'],
    }

    import sys

    sys.modules[__name__] = LazyImportModule(
        __name__,
        globals()['__file__'],
        _import_structure,
        module_spec=__spec__,
        extra_objects={},
    )
