#!/usr/bin/python
# @Time     : 2019/3/1 13:48
# @Author   : linlianyu
# @File     : TestThread.py
import threading, time


def thread_stop():
    for i in range(1, 6):
        print('线程第 %s 次暂停' % i)
        time.sleep(1)


threadObj = threading.Thread(target=thread_stop())
threadObj.start()
print('线程结束')
# 错误写法
# threadObj = threading.Thread(target=print('1', '2', '3', sep='&'))
threadObj = threading.Thread(target=print, args=['1', '2', '3'], kwargs={'sep': '&'})
threadObj.start()
