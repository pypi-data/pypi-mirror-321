#!/usr/bin/env python
# encoding: utf-8
# Copyright (c) 2024- MAGO
# AUTHORS:
# Sukbong Kwon (Galois)

import pandas as pd
from datetime import datetime
from typing import Dict, Text


def display_voice_separation(
    data: Dict,
    query: Text,
)-> None:
    """Display subtitle generation"""
    # Load data
    # DataFrame 생성
    pd.set_option('display.max_colwidth', 20)
    df = pd.DataFrame(data)

    # s2t에서 decodingTime과 text를 병합하여 새로운 열로 추가
    # Text만 추가
    df["vocals"] = df["intrumentFiles"].apply(lambda x: x["vocals"])
    # df["s2t_info"] = df["s2t"].apply(lambda x: f"Decoding Time: {x['decodingTime']}, Text: {x['text']}")

    # 원하는 열만 선택하여 새로운 DataFrame 생성
    selected_columns = df[["id", "filePath", "vocals", "createdAt"]]

    # 출력
    if query == "last":
        display_last(selected_columns)
    elif query == "today":
        display_today(selected_columns)
    else:
        print(selected_columns)


def display_last(
    df: pd.DataFrame,
)-> None:
    # Check if the DataFrame is empty
    if df.empty:
        print("No data available")
        return

    """Get last subtitle generation"""
    pd.set_option('display.max_colwidth', 80)
    last_data = df.iloc[-1]
    print(last_data)


def display_today(
    df: pd.DataFrame,
)-> None:
    """Get today subtitle generation"""
    # 오늘 날짜와 같은 항목 필터링
    df['createdAt'] = pd.to_datetime(df['createdAt'])
    today = pd.to_datetime(datetime.now().date())  # 오늘의 날짜 (시간 없음)
    filtered_df = df[df['createdAt'].dt.date == today.date()]
    print(filtered_df)