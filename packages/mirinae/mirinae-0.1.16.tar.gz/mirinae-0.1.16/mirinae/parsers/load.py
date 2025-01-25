#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2024- MAGO
# AUTHORS:
# Sukbong Kwon (Galois)

from .common import add_common_arguments
from .user import user_subparser
from .product import product_subparser
from .project import project_subparser
from .flow import flow_subparser

def load_parser(parser):

    # Common options
    add_common_arguments(parser)

    # Subparsers & use common options
    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
        help="Command to execute",
    )
    user_subparser(subparsers)
    product_subparser(subparsers)
    project_subparser(subparsers)
    flow_subparser(subparsers)


