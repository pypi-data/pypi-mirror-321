#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2024- MAGO
# AUTHORS:
# Sukbong Kwon (Galois)

import json
import requests
from typing import Dict
from pathlib import Path

# Local
from ..config import FRAMEWORK_ENDPOINT, HEADERS
from ..utils import show_response
from ..auth import ACCESS_TOKEN_PATH, REFRESH_TOKEN_PATH

def login(args) -> Dict:
    """Login

    Args:
        email: Text - Email
        password: Text - Password
        verbose: bool - Verbose mode
    """
    email = args.email
    password = args.password
    verbose = args.verbose

    url = f"{FRAMEWORK_ENDPOINT}/login"

    response = requests.post(
        url,
        headers=HEADERS,
        json={
            'email': email,
            'password': password
        },
    )

    # When the response is successful
    # `refresh_token` and `access_token` are stored in a file
    if response.status_code == 200:
        # Save the refresh token
        set_cookie = response.headers.get('Set-Cookie')
        Path(REFRESH_TOKEN_PATH).parent.mkdir(parents=True, exist_ok=True)
        open(REFRESH_TOKEN_PATH, 'w').write(json.dumps({'Set-Cookie': set_cookie}, indent=4, ensure_ascii=False))

        # Save the access token
        Path(ACCESS_TOKEN_PATH).parent.mkdir(parents=True, exist_ok=True)
        open(ACCESS_TOKEN_PATH, 'w').write(json.dumps(response.json(), indent=4, ensure_ascii=False))

    if verbose:
        show_response("Login", url, response)

    return response