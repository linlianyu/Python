#!/usr/bin/python
# @Time     : 2019/1/25 13:34
# @Author   : linlianyu
# @File     : ErrorExample.py
import traceback


def one():
    two()


def two():
    raise Exception('123456789')


try:
    one()
except:
    # 打开错误信息文件
    errorFile = open('ErrorInfo.txt', 'w')
    # 将错误信息写进文件中
    errorFile.write(traceback.format_exc())
    print('错误信息已经写进 ErrorInfo.txt 文件中')
