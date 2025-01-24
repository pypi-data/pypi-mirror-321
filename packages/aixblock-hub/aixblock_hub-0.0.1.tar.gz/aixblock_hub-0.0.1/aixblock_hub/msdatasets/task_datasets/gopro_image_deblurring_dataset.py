# Copyright (c) AIxBlock, Inc. 

from aixblock_hub.msdatasets.dataset_cls.custom_datasets import \
    GoproImageDeblurringDataset
from aixblock_hub.utils.logger import get_logger

logger = get_logger()
logger.warning(
    'The reference has been Deprecated in aixblock v1.4.0+, '
    'please use `from aixblock_hub.msdatasets.dataset_cls.custom_datasets import GoproImageDeblurringDataset`'
)
