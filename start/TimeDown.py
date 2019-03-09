#!/usr/bin/python
# @Time     : 2019/3/1 22:43
# @Author   : linlianyu
# @File     : TimeDown.py
import time
second = 60
while second > 0:
    print(second)
    time.sleep(1)
    second -= 1
print('倒计时结束')
