#！/usr/bin/env python
#_*_conding:dtf-8_*_
# @Time    : 2019/1/15 0015 上午 10:48
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : mouse_drag.py

from  selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver=webdriver.Chrome()
driver.get("https://mail.163.com/")

#登录快播私有云
driver.find_element_by_id("user_name").send_keys("18576437695")
driver.find_element_by_id("user_pwd").send_keys("zhang199217")
driver.find_element_by_id("dl_an_submit").click()

#定位元素的原位置
element=driver.find_element_by_class_name("source")
#定位元素要移动的目标位置
target=driver.find_element_by_name("target")
#执行元素的移动操作
ActionChains(driver).drag_and_drop(element,target).perform()
time.sleep(3)

driver.close()
