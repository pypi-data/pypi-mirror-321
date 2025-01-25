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

def get(args) -> Dict:
    """Get project information

    Args:
        id: Text - Project ID
        name: Text - Project name
        verbose: bool - Verbose mode

    >>> mirinae project get -v
    >>> mirinae project get -v -id <project_id>
    >>> mirinae project get -v --name <project_name>
    """
    # Set the URL
    url = f"{FRAMEWORK_ENDPOINT}/project"

    # Update the URL with input parameters
    if args.id:
        url = url + f"?projectId={args.id}"
    if args.name:
        url = url + f"?name={args.name}"

    # Send the request
    response = requests.get(
        url,
        headers=get_header_from_token(),
    )

    # Display the response
    if args.verbose:
        show_response("Get", url, response)

    return response
