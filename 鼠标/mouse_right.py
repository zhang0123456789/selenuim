#！/usr/bin/env python
#_*_conding:dtf-8_*_
# @Time    : 2019/1/15 0015 上午 9:45
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : mouse_right.py


from  selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver=webdriver.Chrome()
driver.get("https://mail.163.com/")

#登录快播私有云
driver.find_element_by_id("user_name").send_keys("18576437695")
driver.find_element_by_id("user_pwd").send_keys("zhang123456")
driver.find_element_by_id("dl_an_submit").click()
time.sleep(3)

#定位到要右击的元素
qqq=driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[3]/table/tbody/tr/td[2]")

#对定位到的元素执行鼠标右键操作
ActionChains(driver).context_click(qqq).perform()
time.sleep(3)


driver.close()