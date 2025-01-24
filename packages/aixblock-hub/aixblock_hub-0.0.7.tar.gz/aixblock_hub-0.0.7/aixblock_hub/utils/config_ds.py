# Copyright (c) AIxBlock, Inc. 

import os
from pathlib import Path

# Cache location
from aixblock_hub.hub.constants import DEFAULT_AIXBLOCK_DATA_ENDPOINT
from aixblock_hub.utils.file_utils import get_aixblock_cache_dir

MS_CACHE_HOME = get_aixblock_cache_dir()

DEFAULT_MS_DATASETS_CACHE = os.path.join(MS_CACHE_HOME, 'hub', 'datasets')
MS_DATASETS_CACHE = Path(
    os.getenv('MS_DATASETS_CACHE', DEFAULT_MS_DATASETS_CACHE))

DOWNLOADED_DATASETS_DIR = 'downloads'
DEFAULT_DOWNLOADED_DATASETS_PATH = os.path.join(MS_DATASETS_CACHE,
                                                DOWNLOADED_DATASETS_DIR)
DOWNLOADED_DATASETS_PATH = Path(
    os.getenv('DOWNLOADED_DATASETS_PATH', DEFAULT_DOWNLOADED_DATASETS_PATH))

HUB_DATASET_ENDPOINT = os.environ.get('HUB_DATASET_ENDPOINT',
                                      DEFAULT_AIXBLOCK_DATA_ENDPOINT)
