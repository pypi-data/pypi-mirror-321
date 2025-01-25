#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2024- MAGO
# AUTHORS:
# Sukbong Kwon (Galois)

import requests
from typing import Dict

# Local
from ..config import FRAMEWORK_ENDPOINT
from ..auth import get_header_from_token
from ..utils import show_response

def update(args) -> Dict:
    """Update a project

    Args:
        id: Text - Project ID
        name: Text - Project name
        description: Text - Project description
        verbose: bool - Verbose mode

    >>> mirinae project update -v -id <id> --name <project_name> --description <project_description>
    """
    # Set the URL
    url = f"{FRAMEWORK_ENDPOINT}/project/{args.id}"

    # Get headers including access token
    headers = get_header_from_token()

    # Set the data to update
    data = {}
    if args.name:
        data["name"] = args.name
    if args.description:
        data["description"] = args.description

    # Send the request
    response = requests.put(
        url,
        headers=headers,
        data=data,
    )

    # Display the response
    if args.verbose:
        show_response("Update", url, response)

    return response
