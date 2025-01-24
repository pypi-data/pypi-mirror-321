# Copyright (c) AIxBlock, Inc. 
from typing import TYPE_CHECKING

from aixblock_hub.utils.import_utils import LazyImportModule

if TYPE_CHECKING:

    from .resnet import ResNet, Bottleneck
    from .splat import SplAtConv2d

else:
    _import_structure = {
        'resnet': ['ResNet', 'Bottleneck'],
        'splat': ['SplAtConv2d']
    }

    import sys

    sys.modules[__name__] = LazyImportModule(
        __name__,
        globals()['__file__'],
        _import_structure,
        module_spec=__spec__,
        extra_objects={},
    )
