#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2024- MAGO
# AUTHORS:
# Sukbong Kwon (Galois)

from .common import add_common_arguments

def project_subparser(subparsers):
    project_parser = subparsers.add_parser(
        "project",
        help="Project options",
    )

    add_common_arguments(project_parser)

    project_subparsers = project_parser.add_subparsers(
        dest="action",
        required=True,
        help="Project actions",
    )

    for action in ["create", "delete", "get", "update", "copy"]:
        action_parser = project_subparsers.add_parser(
            action,
            help=f"{action.capitalize()} project",
        )

        # Add common arguments to each action parser
        add_common_arguments(action_parser)


