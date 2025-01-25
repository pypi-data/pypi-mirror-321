#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2024- MAGO
# AUTHORS:
# Sukbong Kwon (Galois)

### Folder ###

import requests
from typing import Dict
from ..config import (
    FRAMEWORK_ENDPOINT,
    HEADERS,
)
from ..utils import get_header_from_token, token_path

message_for_params = """
mirinae folder get --id <folder ID>
    --id: Folder ID to get (optional, default: root)
"""

def info(
    params,
)-> Dict:
    # Check the parameters
    if params.id is None:
        folder_id = "root"
    else:
        folder_id = params.id


    # Set url and headers
    url = f"{FRAMEWORK_ENDPOINT}/folder/{folder_id}"
    headers = get_header_from_token(token_path)

    response = requests.get(
        url,
        headers=headers,
    )

    return url, response