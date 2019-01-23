#！/usr/bin/env python
#_*_conding:dtf-8_*_
# @Time    : 2019/1/15 0015 上午 10:56
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : first_method.py

from  selenium import webdriver
import time,os

driver=webdriver.Chrome()
file_path='file:///'+os.path.abspath("checkbox.html")
driver.get(file_path)

#选择页面上所有的input ，然后从中过滤出所有的checkbox并勾选
inputs=driver.find_element_by_tag_name('input')

for input in inputs:
    if input.get_attribute('type')=='checkbox':
        input.click()
time.sleep(2)


driver.quit()