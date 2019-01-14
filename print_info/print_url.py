#！/usr/bin/env python
#_*_conding:dtf-8_*_
# @Time    : 2019/1/14 0014 下午 18:00
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : print_url.py

from  selenium import  webdriver
import time
browser=webdriver.Chrome()
url="http://www.baidu.com"
print( "now access %s" %(url))
browser.get(url)#通过get方法获取当前url打印
time.sleep(2)


browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
time.sleep(3)

browser.quit()