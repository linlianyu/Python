#!/usr/bin/python
# @Time     : 2019/2/28 20:30
# @Author   : linlianyu
# @File     : TestLoads.py
import json
jsonData = '{"name": "linlianyu", "age": 22, "sex": "boy"}'
# 返回一个 Python 字典
jsonDataValue = json.loads(jsonData)
print(jsonDataValue)
