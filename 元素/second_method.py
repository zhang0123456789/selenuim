#！/usr/bin/env python
#_*_conding:dtf-8_*_
# @Time    : 2019/1/15 0015 上午 11:02
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : second_method.py


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

#打印当前页面有多少个checkbox
print(len(driver.find_element_by_css_selector('input[type=checkbox]')))
time.sleep(2)

driver.quit()