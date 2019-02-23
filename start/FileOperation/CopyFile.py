#!/usr/bin/python
# @Time     : 2018/12/1 13:57
# @Author   : linlianyu
# @File     : CopyFile.py
import shutil, os
copy1 = './HighFileHandle/TestCopy1/'
copy2 = './HighFileHandle/TestCopy2/'
fileName = '1.txt'
if os.path.isfile(copy1):
    shutil.copy(copy1 + fileName, copy2 + fileName)
    print('文件复制成功')
else:
    if not os.path.exists(copy1):
        os.makedirs(copy1)
        file = open(copy1 + fileName, 'w')
        file.write('123')
        file.close()
        print('目录与文件创建成功')
    else:
        file = open(copy1 + fileName, 'w')
        file.write('123')
        file.close()
        print('目录与文件创建成功')
    shutil.copy(copy1 + fileName, copy2 + fileName)
    print('文件复制成功')

