# Copyright (c) AIxBlock, Inc. 
from typing import TYPE_CHECKING

from aixblock_hub.utils.import_utils import LazyImportModule

if TYPE_CHECKING:
    from .nerf_recon_vq_compression import NeRFReconVQCompression
    # from .nerf_preprocess import NeRFReconPreprocessor

else:
    _import_structure = {
        'nerf_recon_vq_compression': ['NeRFReconVQCompression']
    }
    # _import_structure = {'nerf_preprocess': ['NeRFReconPreprocessor']}

    import sys

    sys.modules[__name__] = LazyImportModule(
        __name__,
        globals()['__file__'],
        _import_structure,
        module_spec=__spec__,
        extra_objects={},
    )
