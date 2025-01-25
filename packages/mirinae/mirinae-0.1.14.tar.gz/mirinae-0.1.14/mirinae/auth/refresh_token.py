#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2024- MAGO
# AUTHORS:
# Sukbong Kwon (Galois)

import requests
import json
from typing import Dict
from pathlib import Path

# Local
from .header import ACCESS_TOKEN_PATH, REFRESH_TOKEN_PATH
from ..config import FRAMEWORK_ENDPOINT, HEADERS
from ..utils import get_logger, show_response

# Define
logger = get_logger(__name__.split('.')[-1])

def regenerate_access_token(
    params,
)-> Dict:
    print (params)
    # Set URL
    url = f"{FRAMEWORK_ENDPOINT}/auth/refreshAccessToken"

    # Copy default headers
    headers = HEADERS.copy()

    # Get the refresh token from the header file
    cookie_data = json.loads(Path(REFRESH_TOKEN_PATH).read_text()).get('Set-Cookie')
    refresh_token = cookie_data.split('=')[1].split(';')[0]

    cookies = {
        "refreshToken": refresh_token
    }

    response = requests.post(url, headers=headers, cookies=cookies)
    # response.raise_for_status()  # Raise an error if the request fails

    # Parse the response
    data = response.json()
    if data.get("status") == "success":
        new_access_token = data["content"]["accessToken"]

        # Save the new access token to the token file
        Path(ACCESS_TOKEN_PATH).parent.mkdir(parents=True, exist_ok=True)
        open(ACCESS_TOKEN_PATH, 'w').write(json.dumps(response.json(), indent=4, ensure_ascii=False))

    else:
        print("Failed to refresh access token:", data.get("message", "Unknown error"))

    if params.verbose:
        show_response("Refresh Access Token", url, response)

    return response