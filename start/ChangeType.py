#!/usr/bin/python
# @Time     : 2018/11/12 14:28
# @Author   : linlianyu
# @File     : ChangeType.py
hello = 'Hello'
liebiao = ['1', '2', 3]
yuanzu = ('1', '2', 3)
print('字符串转换为列表和元组')
strList = list(hello)
strTuple = tuple(hello)
print(strList)
print(strTuple)
print('-----这是一条可爱的分割线-----')
print('列表转换为元组')
listTuple = tuple(liebiao)
print(listTuple)
print('-----这是一条可爱的分割线-----')
print('元组转换为列表')
tupleList = list(yuanzu)
print(tupleList)
print('End')
