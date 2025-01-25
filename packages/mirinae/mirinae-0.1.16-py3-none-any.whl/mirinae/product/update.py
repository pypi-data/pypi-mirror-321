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

def update(args) -> Dict:
    """Update a product
    - In product management, the product ID means the product name.
    - Product update is only available for the product owner.
    - Product is updated with a new JSON file.

    Args:
        id: Text - Product ID
        file: Text - Service product JSON file

    >>> mirinae product update -v -f product.json -id audion_emo
    """
    # Set the URL
    url = f"{FRAMEWORK_ENDPOINT}/product/{args.id}"

    # Set headers
    headers = HEADERS.copy()

    # Send the request
    response = requests.put(
        url,
        headers=headers,
        files={
            'file': open(args.file, 'rb'),
        },
    )

    # Display the response
    if args.verbose:
        show_response("Update", url, response)

    return response
