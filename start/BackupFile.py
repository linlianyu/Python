#!/usr/bin/python
# @Time     : 2018/10/16 23:25
# @Author   : linlianyu
# @File     : BackupFile.py
import os
import time
# 进入文件夹的命令
cd = 'cd /Volumes/linlianyu/'
# 需要备份的文件或文件夹
source = 'Python'
# 备份文件存放的路径
target = '/Users/linlianyu/Desktop/' + time.strftime('%Y%m%d')
# 判断路径是否存在
if not os.path.exists(target):
    os.mkdir(target)    # 生成这个路径
# 备份文件的绝对路径
target = target + os.sep + time.strftime('%H%M%S') + '.zip'
# 备份文件的命令
command = cd+'\nzip -qr %s %s' % (target, source)
if os.system(command) == 0:
    print('备份成功')
else:
    print('备份失败')
