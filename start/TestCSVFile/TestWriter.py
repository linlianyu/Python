#!/usr/bin/python
# @Time     : 2019/2/27 22:53
# @Author   : linlianyu
# @File     : TestWriter.py
import csv
outputFile = open('File/TestWriter.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow([9, 8, 7])
outputWriter.writerow([6, 5, 4])
outputWriter.writerow([3, 2, 1])
outputFile.close()
