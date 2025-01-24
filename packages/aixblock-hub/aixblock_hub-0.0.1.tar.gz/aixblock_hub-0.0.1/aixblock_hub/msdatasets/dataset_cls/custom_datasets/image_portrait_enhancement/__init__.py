# Copyright (c) AIxBlock, Inc. 
from typing import TYPE_CHECKING

from aixblock_hub.utils.import_utils import LazyImportModule

if TYPE_CHECKING:
    from .image_portrait_enhancement_dataset import ImagePortraitEnhancementDataset

else:
    _import_structure = {
        'image_portrait_enhancement_dataset':
        ['ImagePortraitEnhancementDataset'],
    }

    import sys

    sys.modules[__name__] = LazyImportModule(
        __name__,
        globals()['__file__'],
        _import_structure,
        module_spec=__spec__,
        extra_objects={},
    )
