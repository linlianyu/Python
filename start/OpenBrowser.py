#!/usr/bin/python
# @Time     : 2019/2/2 22:19
# @Author   : linlianyu
# @File     : OpenBrowser.py
import webbrowser, requests, bs4, prettytable
# import urllib.request, ssl, webbrowser, prettytable
# ssl._create_default_https_context = ssl._create_unverified_context
# page = urllib.request.urlopen('https://movie.douban.com/top250?format=text')
# htmlText = page.read()
# soup = bs4.BeautifulSoup(htmlText, 'html.parser')
# 利用 requests.get()函数把网页下载
page = requests.get('https://movie.douban.com/top250?format=text')
# 加载 HTML 文件
soup = bs4.BeautifulSoup(page.text, 'html.parser')
print('豆瓣电影TOP250')
# 表格打印
x = prettytable.PrettyTable(['电影名', '评分', '评论人数', '链接'])
# 查找所需的元素
for i in soup.find_all('div', class_='info'):
    name = i.find('span', class_='title').get_text()
    score = i.find('span', class_='rating_num').get_text()
    people = i.find('div', class_='star').findAll('span')[3].contents[0]
    url = i.find('a').get('href')
    x.add_row([str(name), str(score), str(people), str(url)])
    # webbrowser.open(url)
print(x)
'''
HTML 部分源码
<div class="info">
    <div class="hd">
        <a href="https://movie.douban.com/subject/1292052/" class="">
            <span class="title">肖申克的救赎</span>
            <span class="title">&nbsp;/&nbsp;The Shawshank Redemption</span>
            <span class="other">&nbsp;/&nbsp;月黑高飞(港)  /  刺激1995(台)</span>
        </a>


        <span class="playable">[可播放]</span>
    </div>
    <div class="bd">
        <p class="">
            导演: 弗兰克·德拉邦特 Frank Darabont&nbsp;&nbsp;&nbsp;主演: 蒂姆·罗宾斯 Tim Robbins /...<br>
            1994&nbsp;/&nbsp;美国&nbsp;/&nbsp;犯罪 剧情
        </p>


        <div class="star">
            <span class="rating5-t"></span>
            <span class="rating_num" property="v:average">9.6</span>
            <span property="v:best" content="10.0"></span>
            <span>1323431人评价</span>
        </div>

        <p class="quote">
            <span class="inq">希望让人自由。</span>
        </p>
    </div>
</div>
'''
