#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2024- MAGO
# AUTHORS:
# Sukbong Kwon (Galois)

import json
import argparse
from typing import Text, Dict
from ..config import (
    FRAMEWORK_ENDPOINT,
    HEADERS,
)
from login import login, session
from ..utils.show import show_response

def subscribe(
    **kwargs,
)-> Dict[Text, Text]:
    url = f"{FRAMEWORK_ENDPOINT}/subscription"
    response = session.post(
        url,
        headers=HEADERS,
        data={
            "serviceName": kwargs.get("serviceName"),
            "planName": kwargs.get("planName"),
        }
    )
    show_response("Subscription", url, response)

def get_with_id(
    id: Text,
)-> None:
    url = f"{FRAMEWORK_ENDPOINT}/subscription/id/{id}"
    response = session.get(
        url,
        headers=HEADERS,
    )
    show_response("Get Subscription with ID", url, response)


def get_with_userId(
    userId: Text,
)-> None:
    url = f"{FRAMEWORK_ENDPOINT}/subscription/user/{userId}"
    response = session.get(
        url,
        headers=HEADERS,
    )
    show_response("Get Subscription with User ID", url, response)


def get_service_names_with_userId(
    userId: Text,
)-> None:
    url = f"{FRAMEWORK_ENDPOINT}/subscription/user/{userId}/serviceNames"
    response = session.get(
        url,
        headers=HEADERS,
    )
    show_response("Get Subscription with User ID", url, response)


def get_with_servicename(
    serviceName: Text,
)-> None:
    url = f"{FRAMEWORK_ENDPOINT}/subscription/service/{serviceName}"
    response = session.get(
        url,
        headers=HEADERS,
    )
    show_response("Get Subscription with Names", url, response)


def update_subscription(
    **kwargs,
)-> None:
    url = f"{FRAMEWORK_ENDPOINT}/subscription"
    response = session.put(
        url,
        headers=HEADERS,
        data={
            "serviceName": kwargs.get("serviceName"),
            "status": kwargs.get("status"),
        }
    )
    show_response("Update Subscription", url, response)

def delete_subscription(
    **kwargs,
)-> None:
    url = f"{FRAMEWORK_ENDPOINT}/subscription"
    response = session.delete(
        url,
        headers=HEADERS,
        data={
            "serviceName": kwargs.get("serviceName"),
        }
    )
    show_response("Delete Subscription", url, response)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--task", dest='task', type=str, default="get")
    parser.add_argument("-s", "--servcie-name", dest='service_name', type=str, default="NONE")
    parser.add_argument("-p", "--plan-name", dest='plan_name', type=str, default="NONE")
    parser.add_argument("-i", "--id", dest='id', type=str, default="NONE")
    parser.add_argument("-u", "--user-id", dest='user_id', type=str, default="NONE")
    parser.add_argument("-d", "--dashboard", action="store_true", help="Show the dashboard")
    args = parser.parse_args()

    # 로그인 후 세션 데이터를 가져옴
    sess_data = login(
        email="galois@holamago.com",
        password="finger2cyg",
    )
    print (json.dumps(sess_data, indent=4, ensure_ascii=False))

    task = args.task

    if task == "subscribe":
        subscribe(
            serviceName=args.service_name,
            planName=args.plan_name,
        )

    if task == "get":
        if args.id != "NONE":
            get_with_id(
                id=args.id,
            )
        if args.user_id != "NONE":
            get_with_userId(
                userId=args.user_id,
            )
        if args.service_name != "NONE":
            get_with_servicename(
                serviceName=args.service_name,
            )

    if task == "services":
        get_service_names_with_userId(
            userId=args.user_id,
        )

    if task == "update":
        update_subscription(
            serviceName=args.service_name,
            status="active",
        )

    if task == "delete":
        delete_subscription(
            serviceName=args.service_name,
        )


if __name__ == '__main__':
    main()
