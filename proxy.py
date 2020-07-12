# !usr/bin/env python
# -*-coding:utf-8 -*-

# @FileName: proxy.py
# @Author:tian
# @Time:07/04/2020

from procuration.db import RedisClient
import sys
import json

# sys.path.append(r'E:\pycharm\project\scrapy_base\procuration')
# print(sys.path)

def reids_client():
    client = RedisClient()
    choice = client.random()
    return choice



if __name__ == '__main__':
    print(reids_client())
