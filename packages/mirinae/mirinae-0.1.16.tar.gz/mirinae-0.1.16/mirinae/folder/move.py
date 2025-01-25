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
mirinae folder move --id <folder ID> --to <destination folder ID>
    --id: Folder ID to move
    --to: Destination folder ID
"""

def move(
    params,
)-> Dict:
    # Check the parameters
    if params.id is None or params.to is None:
        print (message_for_params)
        return None, None

    # Set url and headers
    url = f"{FRAMEWORK_ENDPOINT}/folder/move/{params.id}"
    headers = get_header_from_token(token_path)

    # Set data
    data = {
        "parentFolderId": params.to,
    }

    response = requests.put(
        url,
        headers=headers,
        data=data,
    )

    return url, response