#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2024- MAGO
# AUTHORS:
# Sukbong Kwon (Galois)

import requests
from typing import Dict

# Local import
from ..config import FRAMEWORK_ENDPOINT
from ..auth import get_header_from_token
from ..utils import show_response

def create(args) -> Dict:
    """Create a project
    - You can get product IDs using 'mirinae product get' command.
    (ex. mirinae product get -v)

    Args:
        id: Text - Product ID
        name: Text - Project name
        verbose: bool - Verbose mode
    Returns:
        Dict: Response

    >>> mirinae project create -v -id <product_id> --name <project_name>
    """
    # Set the URL
    url = f"{FRAMEWORK_ENDPOINT}/project/{args.id}"

    # Get headers including access token
    headers = get_header_from_token()

    # Send the request
    project_name = args.name if args.name else ""
    response = requests.post(
        url,
        headers=headers,
        data={
            "name": project_name
        }
    )

    # Display the response
    if args.verbose:
        show_response("Create", url, response)

    return response