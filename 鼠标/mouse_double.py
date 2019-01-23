#！/usr/bin/env python
#_*_conding:dtf-8_*_
# @Time    : 2019/1/15 0015 上午 10:45
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : mouse_double.py


from  selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver=webdriver.Chrome()
driver.get("https://mail.163.com/")

#登录快播私有云
driver.find_element_by_id("user_name").send_keys("18576437695")
driver.find_element_by_id("user_pwd").send_keys("zhang199217")
driver.find_element_by_id("dl_an_submit").click()

#定位到要双击的元素
qqq=driver.find_element_by_xpath("sss")
#对定位的元素执行鼠标双击操作
ActionChains(driver).double_click(qqq).perform()
time.sleep(3)

driver.close()