#!/usr/bin/python
# @Time     : 2019/2/28 14:38
# @Author   : linlianyu
# @File     : DeleteHead.py
import csv, os
# 遍历文件夹下的所有文件
for csvFileName in os.listdir('File/HaveHead/.'):
    if not csvFileName.endswith('.csv'):
        continue
    print('删除' + csvFileName + '文件的表头')
    csvData = []
    file = open('File/HaveHead/' + csvFileName)
    csvReader = csv.reader(file)
    for row in csvReader:
        if csvReader.line_num == 1:
            continue
        csvData.append(row)
    file.close()
    outputFile = open('File/DeleteHead/' + csvFileName, 'w', newline='')
    outputWriter = csv.writer(outputFile)
    for row in csvData:
        outputWriter.writerow(row)
    outputFile.close()
