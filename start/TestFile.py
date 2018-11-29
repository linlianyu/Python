#!/usr/bin/python
# @Time     : 2018/11/28 21:55
# @Author   : linlianyu
# @File     : TestFile.py
import os
print(os.getcwd())      # 获取当前的工作目录
print('-----这是一条可爱的分割线-----')
# folder = os.path.join('/Users', 'linlianyu', 'Downloads', 'Test')
# os.makedirs(folder)       # 创建文件夹
print('-----这是一条可爱的分割线-----')
print(os.path.abspath('.'))     # 获取传入目录的完全路径
print(os.path.isabs('.'))       # 判断传入目录是否为完全路径
print(os.path.isabs(os.path.abspath('.')))
# os.path.relpath(end,start)将返回从start路径到end路径的相对路径,不传入start则使用当前工作路径作为开始路径
print(os.path.relpath('/User/linlianyu/DowDownloads', '/Users/linlianyu/github/Python/start'))
print(os.path.relpath('/User/linlianyu/DowDownloads'))
print('-----这是一条可爱的分割线-----')
path = '/User/linlianyu/github/Python/start/TestFile.py'
print(os.path.basename(path))       # 返回传入路径的基本名称
print(os.path.dirname(path))        # 返回传入路径的目录名称
name1 = os.path.split(path)      # 使用os.path.split()方法获得传入路径的目录名称和基本名称的元组
print(name1)
name2 = path.split(os.path.sep)      # 利用程序运行系统的斜杠来分割路径,并存入列表
print(name2)        # OS X和Linux系统上,返回的列表头都有一个空字符串
print('-----这是一条可爱的分割线-----')
print(os.path.getsize('./TestFile.py'))     # 获取文件的字节数
print(os.listdir('.'))      # 查看目录下的所有文件
size = 0
for fileName in os.listdir('.'):
    size += os.path.getsize(os.path.join('.', fileName))
print(size)
