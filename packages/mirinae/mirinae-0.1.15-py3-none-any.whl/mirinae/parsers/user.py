#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2024- MAGO
# AUTHORS:
# Sukbong Kwon (Galois)

from .common import add_common_arguments

def user_subparser(subparsers):
    user_parser = subparsers.add_parser(
        "user",
        help="User options",
    )

    add_common_arguments(user_parser)

    user_subparsers = user_parser.add_subparsers(
        dest="action",
        required=True,
        help="User actions",
    )

    for action in ["login", "logout", "signup", "update", "delete", "refresh"]:
        action_parser = user_subparsers.add_parser(
            action,
            help=f"{action.capitalize()} user",
        )

        # Add common arguments to each action parser
        add_common_arguments(action_parser)

        action_parser.add_argument(
            "-e",
            "--email",
            help="Email",
            type=str,
        )

        action_parser.add_argument(
            "-pw",
            "--password",
            help="Password",
            type=str,
        )

        action_parser.add_argument(
            "-u",
            "--username",
            help="Username",
            type=str,
        )

        action_parser.add_argument(
            "--organization",
            help="Organization",
            type=str,
        )

        action_parser.add_argument(
            "--job_title",
            help="Job title",
            type=str,
        )

        action_parser.add_argument(
            "--role",
            help="Role (admin, user, ...)",
            type=str,
        )

        action_parser.add_argument(
            "--status",
            help="Status (active, inactive, ...)",
            type=str,
        )