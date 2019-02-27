#!/usr/bin/python
# @Time     : 2019/2/23 21:55
# @Author   : linlianyu
# @File     : Test.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser = webdriver.Firefox()
browser.get('http://www.taobao.com')
input_first = browser.find_element(By.ID, 'q')
input_first.send_keys('ipad')
time.sleep(1)
input_first.clear()
input_first.send_keys('macbook')
browser.close()
