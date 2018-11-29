#!/usr/bin/python
# @Time     : 2018/11/29 16:21
# @Author   : linlianyu
# @File     : TestShelve.py
import shelve
shelveFile = shelve.open('MyData')      # 打开一个shelf文件,会自动生成一个.db文件,window下生成.bak, .dat, .dir三个文件
me = ['lin', 'lian', 'yu']
you = ['da', 'sha', 'zi']
shelveFile['me'] = me       # 将变量存入shelf文件中
shelveFile['you'] = you
print(type(shelveFile))
print(shelveFile['me'])     # 读取文件中的变量
print(shelveFile['you'])
print(list(shelveFile.keys()))      # shelf文佳就像字典一样,有keys()和values()方法
print(list(shelveFile.values()))
print(list(shelveFile.get('me')))       # 获取键所对应的值
print(list(shelveFile.get('you')))
shelveFile.close()
