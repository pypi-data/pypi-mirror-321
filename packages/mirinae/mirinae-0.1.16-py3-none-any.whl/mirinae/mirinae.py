#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2024- MAGO
# AUTHORS:
# Sukbong Kwon (Galois)

# Mirinae CLI for Audion

import importlib
import argparse

# Local
from .parsers.load import load_parser
from .utils.set_logging import get_logger
from .utils.show import show_status

# Define
logger = get_logger(__name__.split('.')[-1])

def main():
    # Define parser
    parser = argparse.ArgumentParser(
        description='Simulator for Mirinae',
        formatter_class=argparse.RawTextHelpFormatter,
        add_help=False,
    )

    # Load parser with subparsers
    load_parser(parser)
    args = parser.parse_args()

    """ Execute command
    - Module is imported dynamically based on the command
    - Action is executed based on the command
    - Arguments are passed to the action

    >>> mirinae <command> <action> <args>
    """
    module = importlib.import_module(f'.{args.command}', package='mirinae')
    getattr(module, args.action)(args)


if __name__ == '__main__':
    main()