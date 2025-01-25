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

def get(args) -> Dict:
    """Get a product
    - Get all products when no arguments are provided
    - Get products by name using regular expression when name is provided
    - Get a product by product ID when product ID is provided

    Args:
        id: Text - Product ID
        verbose: bool - Verbose mode

    >>> mirinae product get -v -id audion_emo
    """
    # Set the URL
    url = f"{FRAMEWORK_ENDPOINT}/product"

    if args.product_id:
        url = url + f"?productId={args.id}"
    if args.name:
        url = url + f"?name={args.name}"

    # Set headers
    headers = HEADERS.copy()

    # Send the request
    response = requests.get(
        url,
        headers=headers,
    )

    # Display the response
    if args.verbose:
        show_response("Get", url, response)

    return response