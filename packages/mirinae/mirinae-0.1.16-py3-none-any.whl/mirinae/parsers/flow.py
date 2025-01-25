#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2024- MAGO
# AUTHORS:
# Sukbong Kwon (Galois)

from .common import add_common_arguments

def flow_subparser(subparsers):
    flow_parser = subparsers.add_parser(
        "flow",
        help="Flow options",
    )

    add_common_arguments(flow_parser)

    flow_subparsers = flow_parser.add_subparsers(
        dest="action",
        required=True,
        help="Flow actions",
    )

    for action in ["run"]:
        action_parser = flow_subparsers.add_parser(
            action,
            help=f"{action.capitalize()} flow",
        )

        # Add common arguments to each action parser
        add_common_arguments(action_parser)
