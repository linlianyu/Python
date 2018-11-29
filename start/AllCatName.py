#!/usr/bin/python
# @Time     : 2018/11/12 13:41
# @Author   : linlianyu
# @File     : AllCatName.py
cats = []
while True:
    name = input('请输入第' + str(len(cats) + 1) + '只猫的名字(按下Enter停止)')
    if name == '':
        break
    else:
        cats = cats + [name]
print('一共有' + str(len(cats)) + '只猫')
for i in range(len(cats)):
    print('第' + str(i+1) + '只猫的名字是:' + cats[i])
