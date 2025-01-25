#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2024- MAGO
# AUTHORS:
# Sukbong Kwon (Galois)

import requests
from typing import Dict

from ..config import FRAMEWORK_ENDPOINT
from ..auth import get_header_from_token
from ..utils import show_response

def run(args) -> Dict:
    """Run a project pipeline

    Args:
        id: Text - Project ID
        input: Text - Input data (uri / url / file)
        input_type: Text - Input type (default: uri)
        folder_id: Text - Folder ID (optional)
        verbose: bool - Verbose mode

    Returns:
        Dict: Response

    >>> mirinae flow run -v -id <flow_id> --input <input_data> --input_type <input_type> --folder_id <folder_id>
    """
    # Set the URL
    url = f"{FRAMEWORK_ENDPOINT}/flow/{args.id}"

    # Get headers including access token
    headers = get_header_from_token()

    # Send the request
    data = {}

    # Set the input type (default: uri)
    if args.input_type:
        data["inputType"] = args.input_type
    else:
        data["inputType"] = "uri"

    # Set the folder ID (if not set, it will be set to the root folder)
    if args.folder_id:
        data["folderId"] = args.folder_id

    # Send the request
    # TODO: Change input data to the multiple data
    if args.input_type == "file":
        # Upload the file from the local path
        response = requests.post(
            url,
            headers=headers,
            data=data,
            files={
                'file': (args.input, open(args.input, 'rb'), f'audio/wav')
            }
        )
    else:
        # Send the input data (url or uri)
        json_data = data
        json_data["input"] = args.input

        response = requests.post(
            url,
            headers=headers,
            json=json_data,
        )

    # Display the response
    if args.verbose:
        show_response("Flow:Run", url, response)

    return response
