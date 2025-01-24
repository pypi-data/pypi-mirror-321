# Copyright (c) AIxBlock, Inc. 

from argparse import ArgumentParser

from aixblock_hub.cli.base import CLICommand
from aixblock_hub.hub.api import HubApi


def subparser_func(args):
    """ Function which will be called for a specific sub parser.
    """
    return LoginCMD(args)


class LoginCMD(CLICommand):
    name = 'login'

    def __init__(self, args):
        self.args = args

    @staticmethod
    def define_args(parsers: ArgumentParser):
        """ define args for login command.
        """
        parser = parsers.add_parser(LoginCMD.name)
        parser.add_argument(
            '--token',
            type=str,
            required=True,
            help='The Access Token for aixblock.')
        parser.set_defaults(func=subparser_func)

    def execute(self):
        api = HubApi()
        api.login(self.args.token)
