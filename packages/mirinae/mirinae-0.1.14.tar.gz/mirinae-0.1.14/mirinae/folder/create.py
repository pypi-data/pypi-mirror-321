#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2024- MAGO
# AUTHORS:
# Sukbong Kwon (Galois)

# Folder

import requests
from typing import Dict
from ..config import (
    FRAMEWORK_ENDPOINT,
    HEADERS,
)
from ..utils import get_header_from_token, token_path

message_for_params = """
mirinae folder create --name <folder name> --to <parent folder ID>
    --name: Folder name
    --to: Parent folder ID (optional, default: root)
"""

def create(
    params,
)-> Dict:
    if params.name is None:
        print (message_for_params)
        return None, None

    url = f"{FRAMEWORK_ENDPOINT}/folder"
    headers = get_header_from_token(token_path)

    data = {
        "name": params.name,
    }
    if params.to:
        data["parentFolderId"] = params.to

    # POST: Create a folder with JSON file
    response = requests.post(
        url,
        headers=headers,
        data=data
    )

    return url, response