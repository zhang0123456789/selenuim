#！/usr/bin/env python
#_*_conding:dtf-8_*_
# @Time    : 2019/1/15 0015 上午 9:35
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : team_keyboard.py


from selenium import webdriver
from  selenium.webdriver.common.keys import Keys
import  time

driver=webdriver.Chrome()

driver.get("http://www.baidu.com")

#输入框输入内容
driver.find_element_by_id("kw").send_keys("selenium")
time.sleep(3)


#ctrl+a全选输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
time.sleep(3)


#ctrl+x剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
time.sleep(3)

#输入框重新输入内容，搜索
driver.find_element_by_id("kw").send_keys("虫师cnblogs")
driver.find_element_by_id("su").click()
time.sleep(3)


driver.quit()
