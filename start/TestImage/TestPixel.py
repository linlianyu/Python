#!/usr/bin/python
# @Time     : 2019/3/2 19:41
# @Author   : linlianyu
# @File     : TestPixel.py
from PIL import Image, ImageColor
import os
os.chdir('File/')
image = Image.new('RGBA', (100, 100))
# 图像上半部分
for x in range(100):
    for y in range(50):
        # 设置每个像素的颜色
        image.putpixel((x, y), (244, 143, 177))
# 图像下半部分
for x in range(100):
    for y in range(50, 100):
        # 获取 red 的 RGB 元组, 然后填充
        image.putpixel((x, y), ImageColor.getcolor('red', 'RGBA'))
image.save('3.png')
