#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2024- MAGO
# AUTHORS:
# Sukbong Kwon (Galois)

from .common import add_common_arguments

def product_subparser(subparsers):
    product_parser = subparsers.add_parser(
        "product",
        help="Product options",
    )

    add_common_arguments(product_parser)

    product_subparsers = product_parser.add_subparsers(
        dest="action",
        required=True,
        help="Product actions",
    )

    for action in ["create", "delete", "get", "update"]:
        action_parser = product_subparsers.add_parser(
            action,
            help=f"{action.capitalize()} product",
        )

        # Add common arguments to each action parser
        add_common_arguments(action_parser)

        action_parser.add_argument(
            "-f",
            "--file",
            help="Service product JSON file",
            type=str,
        )