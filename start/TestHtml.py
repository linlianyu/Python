#!/usr/bin/python
# @Time     : 2019/2/3 14:44
# @Author   : linlianyu
# @File     : TestHtml.py
import bs4
exampleFile = open('Test.html')
exampleSoup = bs4.BeautifulSoup(exampleFile, 'html.parser')
print(type(exampleSoup))
p = exampleSoup.select('p')
p0 = p[0]
p1 = p[1]
print(str(p0))
print(p0.getText())
print(str(p1))
print(p1.getText())
print(str(p0.get('id')))
print(str(p1.get('id')))
