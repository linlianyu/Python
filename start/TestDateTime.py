#!/usr/bin/python
# @Time     : 2019/3/1 13:30
# @Author   : linlianyu
# @File     : TestDateTime.py
import datetime, time
# 返回当前的时间
print(datetime.datetime.now())
# 传入指定的年月日时分秒
dt = datetime.datetime(2019, 3, 1, 12, 0, 0)
print(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
# 返回指定时间戳的时间
print(datetime.datetime.fromtimestamp(1000))
# 与datetime.datetime.now()功能相同
print(datetime.datetime.utcfromtimestamp(time.time()))

