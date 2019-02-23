#!/usr/bin/python
# @Time     : 2019/1/25 13:19
# @Author   : linlianyu
# @File     : TestException.py


def exception(width, height):
    if width == 0 & height == 0:
        raise Exception('长或宽不能为0')
    else:
        print('长方形的面积为:' + str(width*height))


try:
    exception(2, 12)
except Exception as err:
    print(str(err))
