#!/usr/bin/python
# @Time     : 2019/2/28 20:41
# @Author   : linlianyu
# @File     : TestDumps.py
import json
pythonData = {'name': 'linlianyu', 'age': 22, 'sex': 'boy'}
jsonData = json.dumps(pythonData)
print(jsonData)
