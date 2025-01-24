# Copyright (c) AIxBlock, Inc. 
from typing import TYPE_CHECKING

from aixblock_hub.utils.import_utils import LazyImportModule

if TYPE_CHECKING:

    from .efficient_stable_diffusion import EfficientStableDiffusion

else:
    _import_structure = {
        'efficient_stable_diffusion': ['EfficientStableDiffusion'],
    }

    import sys

    sys.modules[__name__] = LazyImportModule(
        __name__,
        globals()['__file__'],
        _import_structure,
        module_spec=__spec__,
        extra_objects={},
    )
