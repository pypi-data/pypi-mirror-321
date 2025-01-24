# Copyright (c) AIxBlock, Inc. 

from typing import TYPE_CHECKING

from aixblock_hub.utils.import_utils import LazyImportModule

if TYPE_CHECKING:
    from .ans_dfsmn_exporter import ANSDFSMNExporter
else:
    _import_structure = {
        'ans_dfsmn_exporter': ['ANSDFSMNExporter'],
    }

    import sys

    sys.modules[__name__] = LazyImportModule(
        __name__,
        globals()['__file__'],
        _import_structure,
        module_spec=__spec__,
        extra_objects={},
    )
