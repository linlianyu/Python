#!/usr/bin/python
# @Time     : 2019/2/27 22:15
# @Author   : linlianyu
# @File     : TestReader.py
import csv
file = open('File/Example.csv')
# Reader 对象只能读取一次,如果需要再次操作,必须重新调用csv.reader()
csvReader = csv.reader(file)
for row in csvReader:
    print('第' + str(csvReader.line_num) + '行: ' + str(row))
