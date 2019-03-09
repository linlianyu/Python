#!/usr/bin/python
# @Time     : 2019/2/28 23:48
# @Author   : linlianyu
# @File     : StopWatch.py
import time
print('按下 Enter 开始计时,再次按下则记录一圈,按下 Ctrl-C 退出程序')
input()
# 用来计算总时间
startTime = time.time()
# 用来计算每一圈的时间
temp = startTime
num = 1
try:
    while True:
        input()
        thisTime = time.time()
        allTime = round(thisTime-startTime, 2)
        watchTime = round(thisTime-temp, 2)
        print('第 %s 圈: %s, 总时: %s' % (num, watchTime, allTime))
        num += 1
        temp = time.time()
except KeyboardInterrupt:
    print('结束')
