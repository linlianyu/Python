#!/usr/bin/python
# @Time     : 2018/11/16 13:42
# @Author   : linlianyu
# @File     : RegularExpression.py
import re       # 导入re模块(正则表达式)
text = 'dsfszd123-456-7890vdszfsdvas'       # 包含电话号码的文本
phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')        # 利用re.compile()函数构建一个Regex对象
mo = phoneNumberRegex.search(text)      # 调用search()方法查找字符串
print('text中的电话号码有:' + mo.group())      # 调用group()方法返回实际匹配文本的字符串
print('-----这是一条可爱的分割线-----')
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')       # 使用()进行分组
mo = phoneNumRegex.search(text)
print('text中的电话号码有:' + mo.group(0) + ';其中区号是:' + mo.group(1) + ',号码是:' + mo.group(2))
print('-----这是一条可爱的分割线-----')
quhao, haoma = mo.groups()      # 调用groups()方法返回所有的分组
print('text中的电话号码有:' + mo.group() + ';其中区号是:' + quhao + ',号码是:' + haoma)
print('-----这是一条可爱的分割线-----')
oneRegex = re.compile(r'one|two')     # 使用管道匹配字符
mo1 = oneRegex.search('one, two, three')        # 返回第一次出现的匹配文本
print(mo1.group())
print('-----这是一条可爱的分割线-----')
twoRegex = re.compile(r'bad(boy|girl|man|women)')       # 指定前缀的文本匹配
mo2 = twoRegex.search('you are a badboy')
print(mo2.group())
print('-----这是一条可爱的分割线-----')
threeRegex = re.compile(r'bad(wo)?man')     # 使用?实现可选匹配文本,?前面的括号的文本可存在也可不存在
mo3 = threeRegex.search('you are a badwoman')
print(mo3.group())
mo3 = threeRegex.search('you are a badman')
print(mo3.group())
print('-----这是一条可爱的分割线-----')
fourRegex = re.compile(r'(wow)*-one')       # 用*号匹配零次或多次文本
mo4 = fourRegex.search('-one')
print(mo4.group())
mo4 = fourRegex.search('wow-one')
print(mo4.group())
mo4 = fourRegex.search('wowwow-one')
print(mo4.group())
mo4 = fourRegex.search('wowwowwow-one')
print(mo4.group())
mo4 = fourRegex.search('wowwowwowwow-one')
print(mo4.group())
print('-----这是一条可爱的分割线-----')
fiveRegex = re.compile(r'(wow)+-one')       # 用+号匹配一次或多次文本
# mo5 = fiveRegex.search('-one')        错误,不能出现0次
# print(mo5.group())
mo5 = fiveRegex.search('wow-one')
print(mo5.group())
mo5 = fiveRegex.search('wowwow-one')
print(mo5.group())
mo5 = fiveRegex.search('wowwowwow-one')
print(mo5.group())
mo5 = fiveRegex.search('wowwowwowwow-one')
print(mo5.group())
print('-----这是一条可爱的分割线-----')
sixRegex = re.compile(r'(wow){3,5}')        # 用{}匹配指定次数
# mo6 = sixRegex.search('wowwow')       错误,不能低于指定次数
# print(mo6.group())
mo6 = sixRegex.search('wowwowwow')
print(mo6.group())
mo6 = sixRegex.search('wowwowwowwowwow')
print(mo6.group())
mo6 = sixRegex.search('wowwowwowwow123')
print(mo6.group())
print('-----这是一条可爱的分割线-----')
sevenRegex = re.compile(r'(wow){3,5}')      # 贪心匹配和非贪心匹配,python默认属于贪心匹配,即匹配字符时会尽量匹配最长的字符串
mo7 = sevenRegex.search('wowwowwowwowwow')
print(mo7.group())
# ?在正则表达式中有两种含义:1、声明非贪心匹配；2、表示可选的分组
sevenRegex = re.compile(r'(wow){3,5}?')     # 非贪心匹配,尽量匹配短的字符串
mo7 = sevenRegex.search('wowwowwowwowwow')
print(mo7.group())
print('-----这是一条可爱的分割线-----')
eightRegex = re.compile(r'\d\d\d-\d\d\d\d-\d\d\d\d')        # findall()方法
mo8 = eightRegex.findall('work: 188-2291-3165 life: 130-4802-5617')     # 将符合的所有字符串都查找出来并存在列表中
print(mo8)
print('-----这是一条可爱的分割线-----')
nineRegex = re.compile(r'\d+\s\w+')
mo9 = nineRegex.findall('1 one, 2 two, 3 three, 4 four, 5 five, 6 six, 7 seven, 8 eight, 9 nine, 10 ten.')
print(mo9)
print('-----这是一条可爱的分割线-----')
tenRegex = re.compile(r'[abcdef]')      # 匹配自定义的字符分组
mo10 = tenRegex.findall('abcdefghijklmnopqrstuvwxyz')
print(mo10)
tenRegex = re.compile(r'[^abcdef]')     # 使用^匹配除了指定字符的所有字符串
mo10 = tenRegex.findall('abcdefghijklmnopqrstuvwxyz')
print(mo10)
print('-----这是一条可爱的分割线-----')
elevenRegex = re.compile(r'^\d')        # 插入字符和美元字符
mo11 = elevenRegex.search('1one')       # 插入字符(^)表示匹配必须在被查文本的开始处
print(mo11 is not None)
elevenRegex = re.compile(r'\d$')        # 美元字符($)表示匹配必须在被查文本的结束处
mo11 = elevenRegex.search('one1')
print(mo11 is None)
print('-----这是一条可爱的分割线-----')
twelveRegex = re.compile(r'.\.mp4')      # 使用通配符(.),匹配除了换行之外的所有字符
mo12 = twelveRegex.findall('1.mp4, 2.mp4, 3.mp4')
print(mo12)
print('-----这是一条可爱的分割线-----')
print('未使用re.DOTALL')
thirteenRegex = re.compile(r'.*')       # 通过传入re.DOTALL作为re.compile()的第二个参数,可以使句号字符匹配包括换行字符的所有字符
mo13 = thirteenRegex.search('123\n456\n789')
print(mo13.group())
print('使用re.DOTALL')
thirteenRegex = re.compile(r'.*', re.DOTALL)
mo13 = thirteenRegex.search('123\n456\n789')
print(mo13.group())
print('-----这是一条可爱的分割线-----')
fourteenRegex = re.compile(r'hello', re.I)      # 通过传入re.I作为re.compile()的第二个参数实现不区分大小写的匹配
mo14 = fourteenRegex.findall('hello, Hello, HELLO')
print(mo14)
print('-----这是一条可爱的分割线-----')
fifteenRegex = re.compile(r'(Hello )(\w)\w+(\w)')       # 使用sub()方法替换字符串
mo15 = fifteenRegex.sub(r'\1\2*****\3', 'Hello linlianyu')      # \1代表第一个分组
print(mo15)
print('-----这是一条可爱的分割线-----')
sixteenRegex = re.compile(r'''      # 通过传入re.VERBOSE作为re.compile()的第二个参数忽略正则表达式字符串中的空白符和注释
        [a-zA-Z0-9.,%*+-]+      # 用户名
        @       # @字符
        [a-zA-Z0-9]+        # 主机名
        (\.[a-zA-Z]{2,4})       # .XXX
    ''', re.VERBOSE)        # 匹配邮箱地址
mo16 = sixteenRegex.search('123564shb@qq.com')
print(mo16)
print('End')
