#！/usr/bin/env python
#_*_conding:dtf-8_*_
# @Time    : 2019/1/14 0014 下午 18:09
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : browser_max.py

from selenium import  webdriver
import  time

browser=webdriver.Chrome()
browser.get("http://www.baidu.com")

print("浏览器最大化")
browser.maximize_window()#将浏览器最大化显示
time.sleep(2)

browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()
time.sleep(3)
browser.quit()
