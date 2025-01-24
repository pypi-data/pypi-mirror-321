"""
Copyright (c) 2024-now LeslieLiang All rights reserved.
Build Date: 2024-12-19
Author: LeslieLiang
Description: API 请求客户端
"""

from __future__ import annotations

from typing import Literal

import requests

from .getter_filter import GetterFilter


class Requester:
    def __init__(self, client: Client, db_name: str):
        self.client = client
        self.db_name = db_name

    def __generate__api_path(
        self, method: Literal['list', 'get', 'create', 'update', 'destroy']
    ):
        """
        生成 API 请求路径

        Args:
            method: 请求方法
        Returns:
            API 请求路径
        """

        return f'{self.client.host}/api/{self.db_name}:{method}'

    def select(self, page=1, page_size=20, filters: GetterFilter = None):
        """
        获取列表数据

        Args:
            page: 页码
            pageSize: 每页数量
        Returns:
            响应数据
        """

        params = {
            'page': page,
            'pageSize': page_size,
        }

        if filters and isinstance(filters, GetterFilter):
            params.update(filters.get_query(flatten=True))

        resp = requests.get(
            self.__generate__api_path('list'),
            headers=self.client.headers,
            params=params,
        )
        resp_json: dict = resp.json()
        return resp_json

    def get(self, filters: GetterFilter = None):
        """
        获取单条数据

        Args:
            filters: 过滤条件
        Returns:
            响应数据
        """

        params = {}
        if filters and isinstance(filters, GetterFilter):
            params.update(filters.get_query(flatten=True))

        resp = requests.get(
            self.__generate__api_path('get'),
            headers=self.client.headers,
            params=params,
        )
        resp_json: dict = resp.json()
        return resp_json

    def create(
        self, record: dict, whitelist: list[str] = None, blacklist: list[str] = None
    ):
        """
        创建数据

        Args:
            record: 要创建的数据
            whitelist: 白名单字段
            blacklist: 黑名单字段
        Returns:
            响应数据
        """

        if not record or not isinstance(record, dict):
            raise ValueError('record type error')

        params = {}
        if whitelist and isinstance(whitelist, list):
            params['whitelist'] = ','.join(whitelist)

        if blacklist and isinstance(blacklist, list):
            params['blacklist'] = ','.join(blacklist)

        resp = requests.post(
            self.__generate__api_path('create'),
            headers=self.client.headers,
            params=params,
            json=record,
        )
        resp_json: dict = resp.json()
        return resp_json

    def update(
        self,
        filters: GetterFilter,
        record: dict,
        whitelist: list[str] = None,
        blacklist: list[str] = None,
    ):
        """
        更新数据

        Args:
            filters: 过滤条件
            record: 要更新的数据
            whitelist: 白名单字段
            blacklist: 黑名单字段
        Returns:
            响应数据
        """

        if not filters or not isinstance(filters, GetterFilter):
            raise ValueError('filters type error')

        if not record or not isinstance(record, dict):
            raise ValueError('record type error')

        params = {}
        if whitelist and isinstance(whitelist, list):
            params['whitelist'] = ','.join(whitelist)

        if blacklist and isinstance(blacklist, list):
            params['blacklist'] = ','.join(blacklist)

        params.update(filters.get_query(flatten=True))

        resp = requests.post(
            self.__generate__api_path('update'),
            headers=self.client.headers,
            params=params,
            json=record,
        )
        resp_json: dict = resp.json()
        return resp_json

    def destroy(self, filters: GetterFilter):
        """
        删除数据

        Args:
            filters: 过滤条件
        Returns:
            响应数据
        """

        if not filters or not isinstance(filters, GetterFilter):
            raise ValueError('filters type error')

        params = filters.get_query(flatten=True)

        resp = requests.post(
            self.__generate__api_path('destroy'),
            headers=self.client.headers,
            params=params,
        )
        resp_json: dict = resp.json()
        return resp_json


class Client:
    def __init__(self, host: str, token: str):
        if not host or not isinstance(host, str):
            raise ValueError('host type error')

        self.host = host.rstrip('/')
        self.token = token
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        }

    def get_requester(self, db_name: str):
        """
        获取请求器对象

        Args:
            db_name: 数据表名称
        Returns:
            请求器对象
        """

        if not db_name or not isinstance(db_name, str):
            raise ValueError('db_name type error')

        return Requester(client=self, db_name=db_name)
