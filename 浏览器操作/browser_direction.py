#！/usr/bin/env python
#_*_conding:dtf-8_*_
# @Time    : 2019/1/14 0014 下午 18:21
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : browser_direction.py


from selenium import  webdriver
import time

browser=webdriver.Chrome()

#访问百度首页
first_url="http://www.baidu.com"
print("now access %s" %(first_url))
browser.get(first_url)
time.sleep(2)

#访问新闻页面
second_url="http://news.baidu.com"
print("now access %s" %(second_url))
browser.get(second_url)
time.sleep(2)

#返回（后退）到百度首页
print("back to %s"%(first_url))
browser.back()
time.sleep(1)
#

#前进到新闻页面
print("forward to %s"%(second_url))
browser.forward()
time.sleep(2)

browser.quit()