# Copyright (c) AIxBlock, Inc. 

from typing import TYPE_CHECKING

from aixblock_hub.utils.import_utils import LazyImportModule

if TYPE_CHECKING:

    from .image_to_video_model import ImageToVideo

else:
    _import_structure = {
        'image_to_video_model': ['ImageToVideo'],
    }

    import sys

    sys.modules[__name__] = LazyImportModule(
        __name__,
        globals()['__file__'],
        _import_structure,
        module_spec=__spec__,
        extra_objects={},
    )
