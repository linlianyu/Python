#!/usr/bin/python
# @Time     : 2019/3/5 16:46
# @Author   : linlianyu
# @File     : TestDrawText.py
from PIL import Image, ImageDraw, ImageFont
import os
image = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(image)
draw.text((50, 50), 'Hello, World!', fill='pink')
textFont = ImageFont.truetype('/Library/Fonts/Comic Sans MS Bold.ttf', 30)
draw.text((0, 60), 'Hello, World!', fill='yellow', font=textFont)
image.save('File/DrawText.png')
