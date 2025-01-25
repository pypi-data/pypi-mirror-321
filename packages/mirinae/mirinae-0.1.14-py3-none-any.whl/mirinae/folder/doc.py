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
mirinae folder add --doc <document ID> --to <folder ID>
    --doc: Document ID
    --act: Action (add, remove)
    --to: Folder ID (optional, default: root)
"""

def doc(
    params,
)-> Dict:
    # Check the parameters
    if params.doc is None or params.act is None:
        print (message_for_params)
        return None, None

    if params.to is None:
        folder = "root"
    else:
        folder = params.to

    # Set url and headers
    url = f"{FRAMEWORK_ENDPOINT}/folder/doc/{folder}"
    headers = get_header_from_token(token_path)

    # Set data
    data = {
        "documentId": params.doc,
        "action": params.act,
    }

    response = requests.put(
        url,
        headers=headers,
        data=data,
    )

    return url, response