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
mirinae folder delete --id <folder ID>
    --id: Folder ID to delete
"""

def delete(
    params,
)-> Dict:
    # Check the parameters
    if params.id is None:
        print (message_for_params)
        return None, None

    # Set url and headers
    url = f"{FRAMEWORK_ENDPOINT}/folder/{params.id}"
    headers = get_header_from_token(token_path)

    response = requests.delete(
        url,
        headers=headers,
    )

    return url, response
