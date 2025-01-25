#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2024- MAGO
# AUTHORS:
# Sukbong Kwon (Galois)


def add_common_arguments(parser):
    parser.add_argument(
        "--version",
        help="Show version and exit",
        action="store_true",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        help="Verbose mode",
        action="store_true",
    )

    parser.add_argument(
        "-d",
        "--debug",
        help="Debug mode",
        action="store_true",
    )

    parser.add_argument(
        "-i",
        "--input",
        help="Input",
        type=str,
    )

    parser.add_argument(
        "-id",
        "--id",
        help="ID", # It could be a project_id, product_id, folder_id, ...
        type=str,
    )

    parser.add_argument(
        "-it",
        "--input-type",
        help="Input type (url, uri, file, text, ...)",
        type=str,
    )

    parser.add_argument(
        "-o",
        "--output",
        help="Output",
        type=str,
    )

    parser.add_argument(
        "-t",
        "--text",
        help="Text",
        type=str,
    )

    parser.add_argument(
        "--name",
        help="Name",
        type=str,
    )

    parser.add_argument(
        "--description",
        help="Description",
        type=str,
    )

    parser.add_argument(
        "-pj",
        "--project_id",
        help="Project ID",
        type=str,
    )

    parser.add_argument(
        "-pd",
        "--product_id",
        help="Product ID",
        type=str,
    )

    parser.add_argument(
        "-fid",
        "--folder_id",
        help="File ID",
        type=str,
    )

    # # Services
    # parser.add_argument("-ns", "--num-speakers", help="Number of speakers", type=int)
    # parser.add_argument("-q", "--query", help="Query", type=str)

    # # Folder
    # parser.add_argument("--field", help="Field", type=str)
    # parser.add_argument("-f", "--folder", help="Folder", type=str)
    # parser.add_argument("-pf", "--parent_folder", help="Parent folder", type=str)
    # parser.add_argument("-to", "--to", help="To", type=str)
    # parser.add_argument("-doc", "--document", help="Document", type=str)

