#!/usr/bin/python
# @Time     : 2019/1/26 13:02
# @Author   : linlianyu
# @File     : TestLogging.py
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')


def wrongjiecheng(n):
    result = 1
    for i in range(n+1):
        result *= i
        logging.debug('i is ' + str(i) + 'result is ' + str(result))
    logging.debug(str(n) + '的阶乘是' + str(result))


def rightjiecheng(n):
    result = 1
    for i in range(1, n+1):
        result *= i
        logging.debug('i is ' + str(i) + 'result is ' + str(result))
    logging.debug(str(n) + '的阶乘是' + str(result))


wrongjiecheng(5)
print('-----这是一条可爱的分割线-----')
rightjiecheng(5)
# 禁用日志信息
# logging.disable(logging.CRITICAL)
