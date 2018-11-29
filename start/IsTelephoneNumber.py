#!/usr/bin/python
# @Time     : 2018/11/16 12:50
# @Author   : linlianyu
# @File     : IsTelephoneNumber.py


def is_phone_number(text):
    if len(text) != 12:
        return False
    for a in range(0, 3):
        if not text[a].isdecimal():
            return False
    if text[3] != '-':
        return False
    for b in range(4, 7):
        if not text[b].isdecimal():
            return False
    if text[7] != '-':
        return False
    for c in range(8, 12):
        if not text[c].isdecimal():
            return False
    else:
        return True


number = '123-456-7890'
print(number + '是一个电话号码:' + str(is_phone_number(number)))

message = 'bhdshabchuavuyuuycbyeBD123-456-7890,NMXJSAHDDYUSjx,.;[]xashx098-765-4321'
for i in range(len(message)):
    number = message[i:i+12]
    if is_phone_number(number):
        print('message中找到电话号码:' + number)
