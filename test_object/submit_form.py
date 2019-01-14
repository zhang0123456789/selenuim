#！/usr/bin/env python
#_*_conding:dtf-8_*_
# @Time    : 2019/1/14 0014 下午 18:35
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : submit_form.py

'''我们把“百度一下”的操作从 click 换成 submit 可以达到相同的'''
from  selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("selenium")
time.sleep(2)

#通过submit（）来操作
driver.find_element_by_id("su").submit()

time.sleep(3)
driver.quit()