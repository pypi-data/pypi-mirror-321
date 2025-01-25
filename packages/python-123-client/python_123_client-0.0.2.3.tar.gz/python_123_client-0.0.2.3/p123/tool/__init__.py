#!/usr/bin/env python3
# encoding: utf-8

__author__ = "ChenyangGao <https://chenyanggao.github.io>"
__all__ = ["make_url", "upload_url"]

from errno import EISDIR
from typing import Literal
from urllib.parse import quote, unquote

from p123 import check_response, P123Client


def make_url(
    client: P123Client, 
    file_id: int,  
) -> str:
    """创建自定义 url，格式为 f"123://{name}|{size}|{md5}"，其中 `name` 已经被 `urllib.parse.quote` 处理过

    :param client: 123 网盘的客户端对象
    :param file_id: 文件 id

    :return: 自定义 url
    """
    resp = check_response(client.fs_info(file_id))
    info = resp["data"]["infoList"][0]
    if info["Type"]:
        raise IsADirectoryError(EISDIR, resp)
    md5 = info["Etag"]
    name = quote(info["FileName"])
    size = info["Size"]
    return f"123://{name}|{size}|{md5}"


def upload_url(
    client: P123Client, 
    url: str, 
    parent_id: int = 0, 
    duplicate: Literal[0, 1, 2] = 0, 
) -> dict:
    """使用自定义链接进行秒传

    :param client: 123 网盘的客户端对象
    :param url: 链接，格式为 f"123://{name}|{size}|{md5}"，前面的 "123://" 可省略，其中 `name` 已经被 `urllib.parse.quote` 处理过
    :param parent_id: 上传到此 id 对应的目录中
    :param duplicate: 处理同名：0: 提醒/忽略 1: 保留两者 2: 替换

    :return: 接口响应，来自 `P123Client.upload_request`，当响应信息里面有 "Reuse" 的值为 "true"，说明秒传成功
    """
    url = url.removeprefix("123://")
    name, size, md5 = url.rsplit("|", 2)
    return client.upload_file_fast(
        file_md5=md5, 
        file_name=unquote(name), 
        file_size=int(size), 
        parent_id=parent_id, 
        duplicate=duplicate, 
    )

