#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@Time    : 2025/1/16 16:22
@Author  : edwinlan
@Email   : edwinlan@tencent.com
@File    : test_sdk.py
"""

import requests
import responses
from responses import matchers

import src.ecom_edwinlan.sdk
from src.ecom_edwinlan.sdk import EComSDK
from src.ecom_edwinlan.models import Product
from src.ecom_edwinlan.models import Config

api_url = "https://example.com"
api_key = "hunter2"


def test_sdk():
    assert src.ecom_sdk.sdk.sdk_function() == "Hello World!"


def test_sdk_class():
    config = Config(api_url="https://example.com", api_key="hunter2")
    sdk = EComSDK(config)
    assert sdk.api_url == config.api_url
    assert sdk.api_key == config.api_key


@responses.activate
def test_sdk_list_stores():
    responses.add(
        responses.GET,
        api_url + "/store",
        json=[
            {"id": 1, "name": "Lidl", "products": 10},
            {"id": 2, "name": "Walmart", "products": 15},
        ],
        status=200,
        match=[matchers.header_matcher({"X-API-KEY": api_key})],
    )

    sdk = EComSDK(api_url, api_key)
    stores = sdk.list_stores()

    assert len(stores) == 2
    assert stores[0]["id"] == 1
    assert stores[0]["name"] == "Lidl"
    assert stores[1]["id"] == 2
    assert stores[1]["name"] == "Walmart"


@responses.activate
def test_sdk_list_stores_connection_error():
    responses.add(
        responses.GET,
        api_url + "/store",
        body=requests.exceptions.ConnectionError(),
    )

    sdk = EComSDK(api_url, api_key)
    try:
        sdk.list_stores()
    except ValueError as err:
        assert "Connection error" in str(err)
    else:
        assert False, "Expected ValueError"


@responses.activate
def test_sdk_list_stores_403():
    responses.add(
        responses.GET,
        api_url + "/store",
        status=403,
    )

    sdk = EComSDK(api_url, api_key)
    try:
        sdk.list_stores()
    except ValueError as err:
        assert "Authentication error" in str(err)
    else:
        assert False, "Expected ValueError"


@responses.activate
def test_sdk_list_products_sort_by_price_desc():
    store_id = 1
    responses.add(
        responses.GET,
        api_url + f"/store/{store_id}/product",
        json=[
            {"id": 1, "name": "Banana", "price": 0.5},
            {"id": 2, "name": "Apple", "price": 0.3},
        ],
        status=200,
        match=[matchers.header_matcher({"X-API-KEY": api_key})],
    )

    sdk = EComSDK(api_url, api_key)
    products = sdk.list_products(store_id, sort_by=EComSDK.ProductSort.PRICE, sort_order=EComSDK.ProductSortOrder.DESC)

    assert len(products) == 2
    assert products[0]["id"] == 1
    assert products[0]["name"] == "Banana"
    assert products[1]["id"] == 2
    assert products[1]["name"] == "Apple"


@responses.activate
def test_sdk_list_products_sort_by_price_desc():
    store_id = 1
    responses.add(
        responses.GET,
        api_url + f"/store/{store_id}/product",
        json=[
            {"id": 1, "name": "Banana", "price": 0.5},
            {"id": 2, "name": "Apple", "price": 0.3},
        ],
        status=200,
        match=[matchers.header_matcher({"X-API-KEY": api_key})],
    )

    sdk = EComSDK(api_url, api_key)
    products = sdk.list_products(store_id, sort_by=EComSDK.ProductSort.PRICE, sort_order=EComSDK.ProductSortOrder.DESC)

    assert len(products) == 2
    assert products[0].id == 1
    assert products[0].name == "Banana"
    assert products[1].id == 2
    assert products[1].name == "Apple"
    assert isinstance(products[0], Product)
    assert isinstance(products[1], Product)

    assert len(products) == 2
    assert products[0].id == 1
    assert products[0].name == "Banana"
    assert products[0].price == 0.5
    assert products[1].id == 2
    assert isinstance(products[0], Product)
    assert isinstance(products[1], Product)
