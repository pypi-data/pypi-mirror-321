#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@Time    : 2025/1/16 16:21
@Author  : edwinlan
@Email   : edwinlan@tencent.com
@File    : sdk.py
"""

import requests
from enum import Enum

from .models import Product
from .models import Config


HTTP_TIMEOUT_SECONDS = 10


class EComSDK:
    def __init__(self, config: Config):
        self.api_url = config.api_url
        self.api_key = config.api_key

    # def list_stores(self):
    #     r = requests.get(
    #         self.api_url + "/store",
    #         headers={"X-API-KEY": self.api_key},
    #         timeout=HTTP_TIMEOUT_SECONDS,
    #     )
    #     if r.status_code == 200:
    #         return r.json()
    #     else:
    #         raise Exception("Invalid response status code: " +
    #                         str(r.status_code))

    def list_stores(self):
        try:
            r = requests.get(
                self.api_url + "/store",
                headers={"X-API-KEY": self.api_key},
                timeout=HTTP_TIMEOUT_SECONDS,
            )
            r.raise_for_status()
        except requests.exceptions.ConnectionError as err:
            raise ValueError("Connection error, check `EComSDK.api_url` is set correctly") from err
        except requests.exceptions.HTTPError as err:
            if err.response.status_code == 403:
                raise ValueError("Authentication error, check `EComSDK.api_key` is set correctly") from err
            else:
                raise

        return r.json()

    class ProductSort(str, Enum):
        PRICE = "price"
        QUANTITY = "quantity"

    class ProductSortOrder(str, Enum):
        DESC = "desc"
        ASC = "asc"

    def list_products(self, store_id, sort_by=ProductSort.PRICE, sort_order=ProductSortOrder.ASC):
        try:
            r = requests.get(
                self.api_url + f"/store/{store_id}/product",
                headers={"X-API-KEY": self.api_key},
                params={"sort_by": sort_by, "sort_order": sort_order},
                timeout=HTTP_TIMEOUT_SECONDS,
            )
            r.raise_for_status()
        except requests.exceptions.ConnectionError as err:
            raise ValueError("Connection error, check `EComSDK.api_url` is set correctly") from err
        except requests.exceptions.HTTPError as err:
            if err.response.status_code == 403:
                raise ValueError("Authentication error, check `EComSDK.api_key` is set correctly") from err
            else:
                raise

        return r.json()

    def list_products1(self, store_id, sort_by=ProductSort.PRICE, sort_order=ProductSortOrder.ASC):
        try:
            r = requests.get(
                self.api_url + f"/store/{store_id}/product",
                headers={"X-API-KEY": self.api_key},
                params={"sort_by": sort_by, "sort_order": sort_order},
                timeout=HTTP_TIMEOUT_SECONDS,
            )
            r.raise_for_status()
        except requests.exceptions.ConnectionError as err:
            raise ValueError("Connection error, check `EComSDK.api_url` is set correctly") from err
        except requests.exceptions.HTTPError as err:
            if err.response.status_code == 403:
                raise ValueError("Authentication error, check `EComSDK.api_key` is set correctly") from err
            else:
                raise

        return [Product(**product) for product in r.json()]


def sdk_function():
    return "Hello World!"
