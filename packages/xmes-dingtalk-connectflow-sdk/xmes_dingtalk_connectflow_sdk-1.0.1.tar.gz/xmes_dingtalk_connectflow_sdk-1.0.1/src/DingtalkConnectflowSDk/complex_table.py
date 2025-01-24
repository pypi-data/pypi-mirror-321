"""
Copyright (c) 2024-now LeslieLiang All rights reserved.
Build Date: 2024-12-18
Author: LeslieLiang
Description: 多维表连接流SDK
"""

import json
from copy import deepcopy
from dataclasses import dataclass
from typing import Literal

from requests import post

from ._types import FilteredDataclass


@dataclass
class GetterFilter:
    """记录筛选器"""

    field: str
    operator: Literal[
        'equal', 'notEqual', 'incontain', 'notContain', 'empty', 'notEmpty'
    ]
    value: list[str] = None


@dataclass
class Updater:
    """记录更新器"""

    record_id: str
    fields: dict[str, any]


@dataclass
class GetterResult(metaclass=FilteredDataclass):
    """获取器结果"""

    nextCursor: str = None
    records: list[dict] = None
    hasMore: bool = False

    def __post_init__(self):
        if self.records and isinstance(self.records, list):
            self.records = self.__records_handle()

    def __records_handle(self):
        records: list[dict] = []
        for record in self.records:
            record_temp = {'id': record.get('id'), 'fields': {}}
            fields: dict = record.get('fields')

            for field_name, field_value in fields.items():
                _value = deepcopy(field_value)
                if isinstance(field_value, dict):
                    if 'link' in field_value:
                        _value = field_value.get('link')
                    elif 'name' in field_value:
                        _value = field_value.get('name')

                record_temp['fields'][field_name] = _value

            records.append(record_temp)

        return records

    def to_file(self, file_path: str):
        """
        将数据写出到本地

        Args:
            file_path: 用于存储数据的文件路径, 不需要文件后缀
        Returns:
            数据文件路径
        """

        if not self.records:
            raise ValueError('数据记录为空, 无法写出')

        with open(f'{file_path}.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(self.records, ensure_ascii=False, indent=2))

        return file_path


class Table:
    __HEADERS = {
        'Content-Type': 'application/json',
    }

    def __init__(self, flow_url: str, did: str, tid: str):
        self.flow_url = flow_url
        self.did = did
        self.tid = tid
        self.global_reqdata = {
            'did': did,
            'tid': tid,
        }

    def get(
        self,
        size=20,
        cursor: str = '',
        combination: Literal['and', 'or'] = 'and',
        filters: list[GetterFilter] | None = None,
    ):
        """
        获取表格数据
        Args:
            size: 每页数据条数, 默认为 20
            cursor: 分页游标, 首次请求可不传, 后续需传入上一次返回的 nextCursor 值
            combination: 组合方式
            filters: 过滤条件
        Returns:
            表格数据
        """

        reqdata = {
            **self.global_reqdata,
            'handle': 'GET',
            'handle_get': {
                'size': size,
                'cursor': cursor,
            },
        }

        if combination and combination in ['and', 'or']:
            filter_field = {}
            filter_field['combination'] = combination
            if filters and isinstance(filters, list):
                conditions = [
                    item.__dict__ for item in filters if isinstance(item, GetterFilter)
                ]
                filter_field['conditions'] = conditions
            reqdata['handle_get']['filter'] = filter_field

        resp = post(self.flow_url, json=reqdata, headers=self.__HEADERS)
        result: dict = resp.json().get('GET_RESULT')

        getter_result = GetterResult(**result)

        return getter_result

    def add(self, records: list[dict]):
        """
        新增记录
        Args:
            records: 新增记录列表
        Returns:
            新增记录结果
        """

        if not records or not isinstance(records, list):
            raise ValueError('records must be a list')

        records_clean = [
            record for record in records if record and isinstance(record, dict)
        ]
        if not records_clean:
            raise ValueError('records must not be empty')

        reqdata = {
            **self.global_reqdata,
            'handle': 'ADD',
            'handle_add': {
                'records': records_clean,
            },
        }

        resp = post(self.flow_url, json=reqdata, headers=self.__HEADERS)
        return resp.json().get('ADD_RESULT')

    def update(self, records: list[Updater]):
        """
        更新记录
        Args:
            records: 更新记录列表
        Returns:
            更新记录结果
        """

        if not records or not isinstance(records, list):
            raise ValueError('records must be a list')

        records_clean = [
            record.__dict__
            for record in records
            if record and isinstance(record, Updater)
        ]
        if not records_clean:
            raise ValueError('records must not be empty')

        reqdata = {
            **self.global_reqdata,
            'handle': 'UPDATE',
            'handle_update': {
                'records': records_clean,
            },
        }

        resp = post(self.flow_url, json=reqdata, headers=self.__HEADERS)
        return resp.json().get('UPDATE_RESULT')

    def delete(self, record_ids: list[str]):
        """
        删除记录
        Args:
            record_ids: 记录 id 列表
        Returns:
            删除记录结果
        """

        if not record_ids or not isinstance(record_ids, list):
            raise ValueError('record_ids must be a list')

        record_ids_clean = [
            record_id
            for record_id in record_ids
            if record_id and isinstance(record_id, str)
        ]

        reqdata = {
            **self.global_reqdata,
            'handle': 'DELETE',
            'handle_delete': {
                'record_ids': record_ids_clean,
            },
        }

        resp = post(self.flow_url, json=reqdata, headers=self.__HEADERS)
        return resp.json().get('DELETE_RESULT')


class ComplexTable:
    def __init__(self, flow_url: str):
        """
        初始化 ComplexTable 类
        Args:
            flow_url: 连接流 url
        """

        self.flow_url = flow_url

    def get_table(self, did: str, tid: str) -> Table:
        """
        获取表格对象
        Args:
            did: 文档 id
            tid: 数据表 id
        Returns:
            Table 对象
        """

        return Table(self.flow_url, did, tid)
