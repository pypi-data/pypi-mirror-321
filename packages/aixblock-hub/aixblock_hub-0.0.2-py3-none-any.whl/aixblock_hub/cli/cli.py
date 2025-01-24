# Copyright (c) AIxBlock, Inc. 

import argparse
import logging

from aixblock_hub.cli.clearcache import ClearCacheCMD
from aixblock_hub.cli.download import DownloadCMD
from aixblock_hub.cli.llamafile import LlamafileCMD
from aixblock_hub.cli.login import LoginCMD
from aixblock_hub.cli.modelcard import ModelCardCMD
from aixblock_hub.cli.pipeline import PipelineCMD
from aixblock_hub.cli.plugins import PluginsCMD
from aixblock_hub.cli.server import ServerCMD
from aixblock_hub.hub.api import HubApi
from aixblock_hub.utils.logger import get_logger

logger = get_logger(log_level=logging.WARNING)


def run_cmd():
    parser = argparse.ArgumentParser(
        'aixblock_hub Command Line tool', usage='aixblock_hub <command> [<args>]')
    parser.add_argument(
        '--token', default=None, help='Specify aixblock platform SDK token.')
    subparsers = parser.add_subparsers(help='aixblock_hub commands helpers')

    DownloadCMD.define_args(subparsers)
    ClearCacheCMD.define_args(subparsers)
    PluginsCMD.define_args(subparsers)
    PipelineCMD.define_args(subparsers)
    ModelCardCMD.define_args(subparsers)
    ServerCMD.define_args(subparsers)
    LoginCMD.define_args(subparsers)
    LlamafileCMD.define_args(subparsers)

    args = parser.parse_args()

    if not hasattr(args, 'func'):
        parser.print_help()
        exit(1)
    if args.token is not None:
        api = HubApi()
        api.login(args.token)
    cmd = args.func(args)
    cmd.execute()


if __name__ == '__main__':
    run_cmd()
