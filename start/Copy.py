#!/usr/bin/python
# @Time     : 2018/11/15 14:11
# @Author   : linlianyu
# @File     : Copy.py
import pyperclip
text = pyperclip.paste()        # 获取剪切板的内容
line = text.split('\n')         # 将获取的内容切割
for i in range(len(line)):      # 在每一行前加一个'*'
    line[i] = '*' + line[i]
text = '\n'.join(line)          # 将列表的内容连接起来
pyperclip.copy(text)            # 将新字符串传递给剪切板
