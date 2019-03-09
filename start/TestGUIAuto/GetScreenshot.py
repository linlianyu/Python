#!/usr/bin/env python3
# @Time     : 2019/3/6 20:08
# @Author   : linlianyu
# @File     : GetScreenshot.py
import pyautogui
image = pyautogui.screenshot()
print(str(image.getpixel((100, 100))))
image.save('123.png')
