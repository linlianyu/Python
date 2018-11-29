#!/usr/bin/python
# @Time     : 2018/11/28 14:47
# @Author   : linlianyu
# @File     : GetPhoneAndEmail.py
"""
测试代码,复制下面字符并运行程序
dshjafgbhjdsfsdf18822913165fjdshfjsdg13048025617nfjksdhfjkasdhf
1825456@1561.com
jsdHcuasdviocjasduifas
jdschjdh@bha.comm
"""
import pyperclip, re
text = str(pyperclip.paste())
phoneRegex = re.compile(r'(1)(3|4|5|6|7|8)(\d{9})')     # 手机号码
result = []
emailRegex = re.compile(r'''(       # 邮箱
        [a-zA-Z0-9.,%*+-]+      # 用户名
        @       # @字符
        [a-zA-Z0-9]+        # 主机名
        (\.[a-zA-Z]{2,4})       # .XXX
    )''', re.VERBOSE)
for phone in phoneRegex.findall(text):      # 匹配手机号码,并将匹配到的字符串添加到元组中
    result.append(''.join([phone[0], phone[1], phone[2]]))
for email in emailRegex.findall(text):  # 匹配邮箱
    result.append(email[0])
if len(result) == 0:        # 检查元组中是否有数据
    print('剪切板中没有找到电话号码或邮箱')
else:
    pyperclip.copy('\n'.join(result))       # 将元组的数据添加到剪切板
    print('已将匹配的电话号码和邮箱添加到剪切板,匹配到的电话号码和邮箱有:')
    print('\n'.join(result))        # 输出元组中的数据
