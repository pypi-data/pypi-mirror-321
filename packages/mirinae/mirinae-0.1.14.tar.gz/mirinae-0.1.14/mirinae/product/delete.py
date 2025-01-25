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

def delete(args) -> Dict:
    """Delete a product
    - Delete a product by product ID

    Args:
        id: Text - Product ID
        verbose: bool - Verbose mode

    >>> mirinae product delete -v -id audion_emo
    """
    # Set the URL
    url = f"{FRAMEWORK_ENDPOINT}/product/{args.id}"

    # Set headers
    headers = HEADERS.copy()

    # Send the request
    response = requests.delete(
        url,
        headers=headers,
    )

    # Display the response
    if args.verbose:
        show_response("Delete", url, response)

    return response
