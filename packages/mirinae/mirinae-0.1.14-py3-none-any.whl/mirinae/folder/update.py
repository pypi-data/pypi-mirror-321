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
mirinae folder update --id <folder ID> --name <folder name>
    --id: Folder ID to update
    --name: Folder name
"""

def update(
    params,
)-> Dict:
    """Update a folder

    Parameters
    ----------
    params.fid : Text
        Folder ID
    """
    # Check the parameters
    if params.id is None or params.name is None:
        print (message_for_params)
        return None, None

    # Set url and headers
    url = f"{FRAMEWORK_ENDPOINT}/folder/name/{params.id}"
    headers = get_header_from_token(token_path)

    # Set data
    data = {
        "name": params.name,
    }

    response = requests.put(
        url,
        headers=headers,
        data=data,
    )

    return url, response