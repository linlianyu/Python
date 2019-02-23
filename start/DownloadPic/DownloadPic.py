#!/usr/bin/python
# @Time     : 2019/2/19 23:19
# @Author   : linlianyu
# @File     : DownloadPic.py
import requests, bs4, os, traceback, time
url = 'http://xkcd.com'
os.makedirs(os.path.join('DownloadPic', 'xkcd'), exist_ok=True)
while not url.endswith('#'):
    # 利用 requests.get()函数把网页下载
    page = requests.get(url)
    print('正在加载网页' + url)
    # 加载 HTML 文件
    soup = bs4.BeautifulSoup(page.text, 'html.parser')
    try:
        pic = soup.select('#comic img')
        picUrl = pic[0].get('src')
        print('正在从' + picUrl + '下载图片')
        page = requests.get('http:' + picUrl)
        picFile = open(os.path.join('DownloadPic', 'xkcd', os.path.basename(picUrl)), 'wb')
        for chunk in page.iter_content(100000):
            picFile.write(chunk)
        picFile.close()
    except:
        errorInfo = open(os.path.join('DownloadPic', 'ErrorInfo.txt'), 'a')
        errorInfo.write(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '\n')
        errorInfo.write(traceback.format_exc())
        fail = open(os.path.join('DownloadPic', 'FailUrl.txt'), 'a')
        fail.write('下载失败的网页是:' + url + '\n')
    prevUrl = soup.select('a[rel=\"prev\"]')[0].get('href')
    url = 'http://xkcd.com' + prevUrl
