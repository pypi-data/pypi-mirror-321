#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2024- MAGO
# AUTHORS:
# Sukbong Kwon (Galois)

import json
from pathlib import Path
from typing import Text

# Define token path
ACCESS_TOKEN_PATH = f"{Path.home()}/.mirinae/access.json"

# Set header path when the token is not available
REFRESH_TOKEN_PATH = f"{Path.home()}/.mirinae/refresh.json"


def get_header_from_token():
    """Get session data header

    Parameters
    ----------
    token_path: Text
        Session data file path

    Returns
    -------
    dict
        Session data header
    """
    if not Path(ACCESS_TOKEN_PATH).exists():
        return {}

    with open(ACCESS_TOKEN_PATH, 'r') as f:
        sess_data = json.load(f)

    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {sess_data.get('content', {}).get('accessToken', '')}"
    }

    return headers