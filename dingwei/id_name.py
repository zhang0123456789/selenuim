#！/usr/bin/env python
#_*_conding:dtf-8_*_
# @Time    : 2019/1/11 0011 下午 18:09
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : id_name.py
import time

from selenium import  webdriver

browser=webdriver.Firefox()

browser.get("http://www.baidu.com")

#通过id方式定位
browser.find_element_by_id('kw').send_keys('selenium')
#通过name方式定位
browser.find_element_by_name('wd').send_keys('selenium')
#通过tag name方式定位
browser.find_element_by_tag_name('input').send_keys('selenium')

#通过class name方式定位
browser.find_element_by_class_name('s_ipt').send_keys('selenium')
# 通过css方式定位
browser.find_element_by_css_selector('#kw').send_keys('selenium')
#通过xphan方式定位
browser.find_element_by_xpath("//input[@id='kw']").send_keys('selenium')

browser.find_element_by_id('su').click()
time.sleep(3)
browser.quit()
