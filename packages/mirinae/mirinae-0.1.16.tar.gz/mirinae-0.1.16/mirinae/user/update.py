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
from ..utils import get_logger, show_response

# Define
logger = get_logger(__name__.split('.')[-1])

def update(args) -> Dict:
    """Update

    Args:
        email: Text - Email
        password: Text - Password
        username: Text - Username
        company: Text - Company
        verbose: bool - Verbose mode

    """
    # Set the URL
    url = f"{FRAMEWORK_ENDPOINT}/user/update"

    # Set headers with access token
    headers = get_header_from_token()

    # Set data
    data = {}
    if args.email:      data['email'] = args.email
    if args.password:   data['password'] = args.password
    if args.username:   data['username'] = args.username
    if args.company:    data['company'] = args.company
    if args.status:     data['status'] = args.status

    # Send the request
    response = requests.put(
        url,
        headers=headers,
        json=data,
    )

    # Display the response
    if args.verbose:
        show_response("Update", url, response)

    return response

