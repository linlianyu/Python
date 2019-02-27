#!/usr/bin/python
# @Time     : 2019/2/27 22:15
# @Author   : linlianyu
# @File     : Test.py
import csv
file = open('File/Example.csv')
csvReader = csv.reader(file)
csvData = list(csvReader)
print(csvData)
for row in csvReader:
    print('第' + str(csvReader.line_num) + '行: ' + str(row))
