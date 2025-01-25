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

def copy(args) -> Dict:
    """Copy a project for customizing with miscro-services

    Args:
        id: Text - Project ID
        verbose: bool - Verbose mode

    Returns:
        Dict: Response

    >>> mirinae project copy -v -id <project_id>
    """
    # Set the URL
    url = f"{FRAMEWORK_ENDPOINT}/project/{args.id}/copy"

    # Get headers including access token
    headers = get_header_from_token()

    # Send the request
    response = requests.post(
        url,
        headers=headers,
    )

    # Display the response
    if args.verbose:
        show_response("Copy", url, response)

    return response