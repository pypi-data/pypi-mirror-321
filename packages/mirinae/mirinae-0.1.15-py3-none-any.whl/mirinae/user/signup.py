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
from ..auth import ACCESS_TOKEN_PATH, REFRESH_TOKEN_PATH

def signup(args) -> Dict:
    """Signup

    Args:
        email: Text - Email
        password: Text - Password
        username: Text - Username
        organization: Text - Organization
        verbose: bool - Verbose mode

    >>> mirinae user signup --email <email> --password <password> --username <username> --organization <organization>
    """
    # Get the arguments
    email = args.email
    password = args.password
    username = args.username
    organization = args.organization
    verbose = args.verbose

    # Set the URL
    url = f"{FRAMEWORK_ENDPOINT}/signup"

    # Set data
    data = {
        'email': email,
        'password': password,
        'username': username,
        'organization': organization,
    }

    # Send the request
    response = requests.post(
        url,
        headers=HEADERS,
        json=data,
    )

    # Display the response
    if verbose:
        show_response("Signup", url, response)

    return response