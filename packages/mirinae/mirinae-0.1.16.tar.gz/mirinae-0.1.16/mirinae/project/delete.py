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

def delete(
    params,
)-> Dict:
    """Delete a project
    - You can get project IDs using 'mirinae project get' command.
    (ex. mirinae project get -v)

    Args:
        id: Text - Project ID
        verbose: bool - Verbose mode
    Returns:
        Dict: Response

    >>> mirinae project delete -v -id <project_id>
    """
    # Set the URL
    url = f"{FRAMEWORK_ENDPOINT}/project/{params.id}"

    # Send the request
    response = requests.delete(
        url,
        headers=get_header_from_token(),
    )

    # Display the response
    if params.verbose:
        show_response("Delete", url, response)

    return response