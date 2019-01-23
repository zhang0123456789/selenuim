#！/usr/bin/env python
#_*_conding:dtf-8_*_
# @Time    : 2019/1/15 0015 上午 11:06
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : leave.py

from  selenium import webdriver
import time,os

driver=webdriver.Chrome()
file_path='file:///'+os.path.abspath("checkbox.html")
driver.get(file_path)

#选择所有的checkbox并全部勾上
checkboxes=driver.find_element_by_css_selector('input[type=checkbox]')
for checkbox in checkboxes:
    checkbox.click()
time.sleep(2)

'''其实，去掉勾选表也逻辑也非常简单，就是再次点击勾选的按钮。可能我们比较迷
惑的是如何找到“最后一个”按钮。pop() 可以实现这个功能'''
#把页面最后一个checkbox的勾去掉
driver.find_element_by_css_selector('input[type=checkbox]').pop().click()
time.sleep(2)

driver.quit()
