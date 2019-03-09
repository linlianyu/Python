#!/usr/bin/python
# @Time     : 2019/3/2 14:06
# @Author   : linlianyu
# @File     : OpenImage.py
from PIL import Image
import os
# 切换工作目录
os.chdir('File/')
myImage = Image.open('2.jpg')
# 打印包含照片宽高像素数的元组
print(myImage.size)
width, height = myImage.size
# 将元组中的值赋给 width 和 height 变量
print('照片的长为 %s, 宽为 %s' % (width, height))
# 打印文件名
print(myImage.filename)
# 打印文件格式
print(myImage.format)
# 另存
myImage.save('2.png')
image1 = Image.new('RGB', (20, 20), 'red')
image1.save('REDImage.jpg')
image2 = Image.new('RGBA', (200, 20))
image2.save('TransparentImage.png')
