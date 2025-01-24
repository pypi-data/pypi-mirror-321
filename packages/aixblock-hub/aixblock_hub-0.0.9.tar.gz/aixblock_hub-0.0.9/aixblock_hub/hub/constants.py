# Copyright (c) AIxBlock, Inc. 

import os
from pathlib import Path

AIXBLOCK_URL_SCHEME = 'https://'
DEFAULT_HUB = os.environ.get('DEFAULT_HUB',  'aixblock')#  huggingface 'modelscope' 'dev-aixblock' 'aixblock'

DEFAULT_AIXBLOCK_DOMAIN = os.environ.get('DEFAULT_AIXBLOCK_DOMAIN',  'app.aixblock.io') #  huggingface.co 'www.modelscope.cn' 'dev-us-west-1.aixblock.io' 'app.aixblock.io'
DEFAULT_AIXBLOCK_DATA_ENDPOINT = AIXBLOCK_URL_SCHEME + DEFAULT_AIXBLOCK_DOMAIN
AIXBLOCK_PARALLEL_DOWNLOAD_THRESHOLD_MB = int(
    os.environ.get('AIXBLOCK_PARALLEL_DOWNLOAD_THRESHOLD_MB', 500))
AIXBLOCK_DOWNLOAD_PARALLELS = int(
    os.environ.get('AIXBLOCK_DOWNLOAD_PARALLELS', 4))
DEFAULT_AIXBLOCK_GROUP = 'aixblock_hub'
MODEL_ID_SEPARATOR = '/'
FILE_HASH = 'Sha256'
LOGGER_NAME = 'AIxBlockHub'
DEFAULT_CREDENTIALS_PATH = Path.home().joinpath('.aixblock', 'credentials')
REQUESTS_API_HTTP_METHOD = ['get', 'head', 'post', 'put', 'patch', 'delete']
API_HTTP_CLIENT_TIMEOUT = 60
API_HTTP_CLIENT_MAX_RETRIES = 2
API_RESPONSE_FIELD_DATA = 'Data'
API_FILE_DOWNLOAD_RETRY_TIMES = 5
API_FILE_DOWNLOAD_TIMEOUT = 60
API_FILE_DOWNLOAD_CHUNK_SIZE = 1024 * 1024 * 1
API_RESPONSE_FIELD_GIT_ACCESS_TOKEN = 'AccessToken'
API_RESPONSE_FIELD_USERNAME = 'Username'
API_RESPONSE_FIELD_EMAIL = 'Email'
API_RESPONSE_FIELD_MESSAGE = 'Message'
AIXBLOCK_CLOUD_ENVIRONMENT = 'AIXBLOCK_ENVIRONMENT'
AIXBLOCK_CLOUD_USERNAME = 'AIXBLOCK_USERNAME'
AIXBLOCK_SDK_DEBUG = 'AIXBLOCK_SDK_DEBUG'
AIXBLOCK_ENABLE_DEFAULT_HASH_VALIDATION = 'AIXBLOCK_ENABLE_DEFAULT_HASH_VALIDATION'
ONE_YEAR_SECONDS = 24 * 365 * 60 * 60
AIXBLOCK_REQUEST_ID = 'X-Request-ID'
TEMPORARY_FOLDER_NAME = '._____temp'


class Licenses(object):
    APACHE_V2 = 'Apache License 2.0'
    GPL_V2 = 'GPL-2.0'
    GPL_V3 = 'GPL-3.0'
    LGPL_V2_1 = 'LGPL-2.1'
    LGPL_V3 = 'LGPL-3.0'
    AFL_V3 = 'AFL-3.0'
    ECL_V2 = 'ECL-2.0'
    MIT = 'MIT'


class ModelVisibility(object):
    PRIVATE = 1
    INTERNAL = 3
    PUBLIC = 5


class DatasetVisibility(object):
    PRIVATE = 1
    INTERNAL = 3
    PUBLIC = 5
