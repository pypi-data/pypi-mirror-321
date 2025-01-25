#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2024- MAGO
# AUTHORS:
# Sukbong Kwon (Galois)

import requests
from typing import Dict
from pathlib import Path

# Local
from ..config import FRAMEWORK_ENDPOINT
from ..auth import get_header_from_token, ACCESS_TOKEN_PATH
from ..utils import show_response

def logout(args) -> Dict:
    """Logout from the server
    """
    url = f"{FRAMEWORK_ENDPOINT}/logout"

    # Set headers with access token
    headers = get_header_from_token()

    # Request logout
    response = requests.post(url, headers=headers)

    # Unlink the access token
    if response.status_code == 200:
        if Path(ACCESS_TOKEN_PATH).exists():
            Path(ACCESS_TOKEN_PATH).unlink()

    # Show response
    if args.verbose:
        show_response("Logout", url, response)

