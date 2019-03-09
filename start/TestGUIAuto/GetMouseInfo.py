#!/usr/bin/env python3
# @Time     : 2019/3/8 23:44
# @Author   : linlianyu
# @File     : GetMouseInfo.py
import pyautogui, time, os
print('按下 Ctrl + C 结束')
try:
    while True:
        x, y = pyautogui.position()
        pixColor = pyautogui.screenshot().getpixel((x, y))
        strColor = '(%s, %s, %s)' % (pixColor[0], pixColor[1], pixColor[2])
        strPosition = 'X: %s, Y: %s, RGB: %s' % (x, y, strColor)
        print(strPosition, end='', flush=True)
        print('\b \b' * len(strPosition), end='')
except KeyboardInterrupt:
    print('\n结束')
