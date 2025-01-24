# Copyright (c) AIxBlock, Inc. 
from typing import TYPE_CHECKING

from aixblock_hub.utils.import_utils import LazyImportModule

if TYPE_CHECKING:
    from .image_quality_assessment_mos_dataset import ImageQualityAssessmentMosDataset

else:
    _import_structure = {
        'image_quality_assessment_mos_dataset':
        ['ImageQualityAssessmentMosDataset'],
    }

    import sys

    sys.modules[__name__] = LazyImportModule(
        __name__,
        globals()['__file__'],
        _import_structure,
        module_spec=__spec__,
        extra_objects={},
    )
