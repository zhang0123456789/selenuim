#！/usr/bin/env python
#_*_conding:dtf-8_*_
# @Time    : 2019/1/14 0014 下午 17:39
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : auto_time.py


from  selenium import webdriver
import  time#调入time函数
browser=webdriver.Chrome()

browser.get("http://www.baidu.com")
browser.implicitly_wait(30)#智能等待30秒,最多等待30s
browser.find_element_by_id("kw").send_keys("selenuim")
browser.find_element_by_id("su").click()

browser.quit()
