#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2024- MAGO
# AUTHORS:
# Sukbong Kwon (Galois)

import requests
from typing import Text, Dict

# Local
from ..config import (
    FRAMEWORK_ENDPOINT,
    HEADERS,
)
from ..utils import get_header_from_token, show_response


def call_dashboard(
    token_path: Text,
    service_name: Text,
    **kwargs,
)-> Dict:
    # 서비스 실행 URL
    url = f"{FRAMEWORK_ENDPOINT}/mydata/{service_name}"

    # 세션 데이터 로드
    headers = get_header_from_token(token_path)

    # 서비스 실행
    response = requests.get(
        url,
        headers=headers,
        data={},
    )
    if kwargs.get('verbose', False):
        show_response(f"Dashboard {service_name}", url, response)
    return response