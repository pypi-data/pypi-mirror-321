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
from ..auth import REFRESH_TOKEN_PATH, ACCESS_TOKEN_PATH
from ..config import FRAMEWORK_ENDPOINT, HEADERS
from ..utils import show_response, get_logger

# Define
logger = get_logger(__name__.split('.')[-1])

def refresh(args) -> Dict:
    """Refresh the user with refresh token

    Args:
        file: Text - Service product JSON file

    >>> mirianae user refresh --verbose
    """
    # Set the URL
    url = f"{FRAMEWORK_ENDPOINT}/auth/refreshAccessToken"

    # Set headers
    headers = HEADERS.copy()

    # Set `cookies` from the `REFRESH_TOKEN_PATH` file
    if not Path(REFRESH_TOKEN_PATH).exists():
        logger.error(f"Refresh token file not found: {REFRESH_TOKEN_PATH}")
        return None

    try:
        cookie_data = json.loads(Path(REFRESH_TOKEN_PATH).read_text()).get('Set-Cookie')
        refresh_token = cookie_data.split('=')[1].split(';')[0]
    except Exception as e:
        logger.error(f"Failed to read refresh token: {e}")
        return None

    # Set the cookies
    cookies = {
        "refreshToken": refresh_token
    }

    # Send the request
    response = requests.post(
        url,
        headers=headers,
        cookies=cookies,
    )

    # Parse the response
    data = response.json()
    if data.get("status") == "success":
        new_access_token = data["content"]["accessToken"]

        # Save the new access token to the token file
        Path(ACCESS_TOKEN_PATH).parent.mkdir(parents=True, exist_ok=True)
        open(ACCESS_TOKEN_PATH, 'w').write(json.dumps(response.json(), indent=4, ensure_ascii=False))
        logger.info("Access token refreshed successfully.")
    else:
        logger.error(f"Failed to refresh access token: {data.get('message', 'Unknown error')}")
        return None

    if args.verbose:
        show_response("Refresh", url, response)

    return response