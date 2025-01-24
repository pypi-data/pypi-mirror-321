# Copyright (c) AIxBlock, Inc. 

import hashlib
import os
from datetime import datetime
from pathlib import Path
from typing import Optional

import requests
from aixblock_hub.hub.constants import DEFAULT_HUB
from aixblock_hub.hub.constants import (DEFAULT_AIXBLOCK_DOMAIN,
                                      DEFAULT_AIXBLOCK_GROUP,
                                      MODEL_ID_SEPARATOR, AIXBLOCK_SDK_DEBUG,
                                      AIXBLOCK_URL_SCHEME)
from aixblock_hub.hub.errors import FileIntegrityError
from aixblock_hub.utils.file_utils import get_default_aixblock_cache_dir
from aixblock_hub.utils.logger import get_logger

logger = get_logger()


def model_id_to_group_owner_name(model_id):
    if MODEL_ID_SEPARATOR in model_id:
        group_or_owner = model_id.split(MODEL_ID_SEPARATOR)[0]
        name = model_id.split(MODEL_ID_SEPARATOR)[1]
    else:
        group_or_owner = DEFAULT_AIXBLOCK_GROUP
        name = model_id
    return group_or_owner, name


# during model download, the '.' would be converted to '___' to produce
# actual physical (masked) directory for storage
def get_model_masked_directory(directory, model_id):
    parts = directory.rsplit('/', 2)
    # this is the actual directory the model files are located.
    masked_directory = os.path.join(parts[0], model_id.replace('.', '___'))
    return masked_directory


def convert_readable_size(size_bytes):
    import math
    if size_bytes == 0:
        return '0B'
    size_name = ('B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f'{s} {size_name[i]}'


def get_folder_size(folder_path):
    total_size = 0
    for path in Path(folder_path).rglob('*'):
        if path.is_file():
            total_size += path.stat().st_size
    return total_size


# return a readable string that describe size of for a given folder (MB, GB etc.)
def get_readable_folder_size(folder_path) -> str:
    return convert_readable_size(get_folder_size(folder_path=folder_path))


def get_cache_dir(model_id: Optional[str] = None):
    """cache dir precedence:
        function parameter > environment > ~/.cache/aixblock/hub
    Args:
        model_id (str, optional): The model id.
    Returns:
        str: the model_id dir if model_id not None, otherwise cache root dir.
    """
    default_cache_dir = Path.home().joinpath('.cache', DEFAULT_HUB) # default cache path modelscope,aixblock,huggingface
    base_path = os.getenv('AIXBLOCK_CACHE',
                          os.path.join(default_cache_dir, 'hub'))
    return base_path if model_id is None else os.path.join(
        base_path, model_id + '/')


def get_release_datetime():
    if AIXBLOCK_SDK_DEBUG in os.environ:
        rt = int(round(datetime.now().timestamp()))
    else:
        from aixblock_hub import version
        rt = int(
            round(
                datetime.strptime(version.__release_datetime__,
                                  '%Y-%m-%d %H:%M:%S').timestamp()))
    return rt


def get_endpoint():
    AIXBLOCK_DOMAIN = os.getenv('AIXBLOCK_DOMAIN',
                                  DEFAULT_AIXBLOCK_DOMAIN)
    return AIXBLOCK_URL_SCHEME + AIXBLOCK_DOMAIN


def compute_hash(file_path):
    BUFFER_SIZE = 1024 * 64  # 64k buffer size
    sha256_hash = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(BUFFER_SIZE)
            if not data:
                break
            sha256_hash.update(data)
    return sha256_hash.hexdigest()


def file_integrity_validation(file_path, expected_sha256):
    """Validate the file hash is expected, if not, delete the file

    Args:
        file_path (str): The file to validate
        expected_sha256 (str): The expected sha256 hash

    Raises:
        FileIntegrityError: If file_path hash is not expected.

    """
    file_sha256 = compute_hash(file_path)
    if not file_sha256 == expected_sha256:
        os.remove(file_path)
        msg = 'File %s integrity check failed, expected sha256 signature is %s, actual is %s, the download may be incomplete, please try again.' % (  # noqa E501
            file_path, expected_sha256, file_sha256)
        logger.error(msg)
        raise FileIntegrityError(msg)
