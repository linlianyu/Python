#!/usr/bin/python
# @Time     : 2019/3/5 22:46
# @Author   : linlianyu
# @File     : TestMouse.py
import pyautogui
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
width, height = pyautogui.size()
print('屏幕的宽为: %s, 高为: %s' % (width, height))
for x, y in zip(range(100, width, 100), range(100, height, 100)):
    pyautogui.moveTo(x, y, duration=0.1)
print('鼠标所在的位置为:' + str(pyautogui.position()))
