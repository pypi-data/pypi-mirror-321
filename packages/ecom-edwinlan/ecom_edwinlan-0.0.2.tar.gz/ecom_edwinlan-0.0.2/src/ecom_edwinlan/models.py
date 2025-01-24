#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@Time    : 2025/1/16 17:14
@Author  : edwinlan
@Email   : edwinlan@tencent.com
@File    : models.py
"""

from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    price: float


class Config(BaseModel):
    api_url: str
    api_key: str
