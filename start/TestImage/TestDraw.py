#!/usr/bin/python
# @Time     : 2019/3/3 21:41
# @Author   : linlianyu
# @File     : TestDraw.py
from PIL import Image, ImageDraw
image = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(image)
# 画点
draw.point([(10, 10), (10, 11), (10, 12), (11, 10), (11, 11), (11, 12), (12, 10), (12, 11), (12, 12)], fill='pink')
# 画线
draw.line([(0, 0), (199, 0), (199, 199), (0, 199), (0, 0)], fill='black', width=5)
# 画矩形
draw.rectangle((20, 20, 50, 40), fill='red')
# 画椭圆
draw.ellipse((20, 20, 50, 40), fill='yellow')
# 画多边形
draw.polygon([(100, 100), (150, 100), (180, 190), (180, 200)], fill='green')
image.save('File/Draw.png')
