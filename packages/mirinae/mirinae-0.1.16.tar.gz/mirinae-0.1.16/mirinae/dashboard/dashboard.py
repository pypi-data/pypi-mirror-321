#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2024- MAGO
# AUTHORS:
# Sukbong Kwon (Galois)

import json
from typing import Any

# Local
from ..user.login import token_path
from ..core import (
    call_dashboard,
)
from ..utils import get_logger
from .subtitle_generation import display_subtitle_generation
from .voice_separation import display_voice_separation

# Define
logger = get_logger(__name__.split('.')[-1])


def dashboard(
    params,
)-> Any:
    # Greeting
    logger.info("Dashboard 호출을 시작합니다.")

    # Set options
    options = {}

    # Get service name
    service_name = params.service_name

    # Dashboard 호출
    if params.get:
        response = call_dashboard(
            token_path=token_path,
            service_name=params.service_name,
            verbose=params.verbose,
            **options,
        )

    # Show response
    width = 100
    if response.status_code == 200:
        # Save response
        save_path = f"{service_name}.json"
        json.dump(response.json(), open(save_path, 'w'), indent=4, ensure_ascii=False)
        logger.info(f"대시보드 데이터를 {save_path}에 저장하였습니다.")
        resp_data = response.json()
        print ("="*width)
        print (f"{params.service_name} Dashboard")
        print ("-"*width)
        print (f"Number of Data: {len(resp_data)}")
        print ("-"*width)


        if service_name == "VoiceSeparation":
            display_voice_separation(
                data=resp_data,
                query=params.query,
            )
        elif service_name == "SubtitleGeneration":
            display_subtitle_generation(
                data=resp_data,
                query=params.query,
            )
        else:
            pass




