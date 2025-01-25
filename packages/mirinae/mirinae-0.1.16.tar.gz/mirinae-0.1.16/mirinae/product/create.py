#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2024- MAGO
# AUTHORS:
# Sukbong Kwon (Galois)

import requests
from typing import Dict

# Local
from ..config import FRAMEWORK_ENDPOINT, HEADERS
from ..utils import show_response

def create(args) -> Dict:
    """Create a product

    Args:
        file: Text - Service product JSON file

    >>> mirinae product create -v -f product.json
    """
    # Set the URL
    url = f"{FRAMEWORK_ENDPOINT}/product"

    # Set headers
    headers = HEADERS.copy()

    # Send the request
    response = requests.post(
        url,
        headers=headers,
        files={
            'file': open(args.file, 'rb'),
        },
    )

    # Display the response
    if args.verbose:
        show_response("Create", url, response)

    return response