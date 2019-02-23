#!/usr/bin/python
# @Time     : 2019/2/3 14:15
# @Author   : linlianyu
# @File     : TestDownload.py
import requests
res = requests.get('''http://file3.data.weipan.cn/\
19378583/324c2cdd295fe8ca5aa7595ac93cdbb8d0d41ba1?\
ip=1549176036,113.117.1.172&ssig=RVSlg3UuZA&Expires=\
1549176636&KID=sae,l30zoo1wmz&fn=%E3%80%90%E5%85%B3%\
E4%BA%8E%E4%B9%A6%E7%94%BB%E7%9A%84%E4%B9%A6%E3%80%91\
%E7%94%BB%E9%A9%AC%E6%8A%80%E6%B3%95%E8%B5%84%E6\
%96%99.pdf&se_ip_debug=113.117.1.172&from=1221134''')
# 检查连接是否成功
print(res.status_code == requests.codes.ok)
# 检查是否下载成功,下载失败则抛出异常
try:
    res.raise_for_status()
except Exception as exc:
    print('错误原因是：%s' % exc)
