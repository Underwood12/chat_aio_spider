# -*- coding: utf-8 -*-
# @时间 : 2020-03-04 22:28
# @作者 : 陈祥安
# @文件名 : config.py
# @公众号: Python学习开发
import toml
from loguru import logger
import traceback
import os

_temp = os.path.dirname(os.path.abspath(__file__))

toml_file = os.path.join(_temp, "config.toml")


def config():
    data = ""
    try:
        with open(toml_file, mode="r", encoding="utf-8") as fs:
            data = toml.load(fs)
    except Exception as e:
        logger.error(f"读取配置错误！:{traceback.format_exc()}")
    return data


if __name__ == '__main__':
    print(config())
