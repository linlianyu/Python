#!/usr/bin/python
# @Time     : 2018/11/12 14:47
# @Author   : linlianyu
# @File     : CopyList.py
import copy
listOne = [1, 2, 3]
listTwo = copy.copy(listOne)
listTwo[1] = 4
print(listOne)
print(listTwo)
print('-----这是一条可爱的分割线-----')
listThree = [[1, 2, 3], [4, 5, 6]]
listFour = copy.deepcopy(listThree)
print(listThree)
print(listFour)
print('End')
