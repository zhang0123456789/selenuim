#！/usr/bin/env python
#_*_conding:dtf-8_*_
# @Time    : 2019/1/14 0014 下午 18:48
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : use_keyboard.py

from  selenium import webdriver
from selenium.webdriver.common.keys import Keys#需要引燃keys包
import  os,time


driver=webdriver.Chrome()
driver.get("http://passport.kuaibo.com/login/?referrer=http%3A%2F%2Fwebcloud.kuaibo.com%2F")
time.sleep(3)
driver.maximize_window()#浏览器全屏显示

driver.find_element_by_id("user_name").clear()
driver.find_element_by_id("user_name").send_keys("fnngj")

#tab的定位相当于清除了密码框的默认提示信息，等同于上面的clear()
driver.find_element_by_id("user_name").send_keys(Keys.TAB)
time.sleep(3)
driver.find_element_by_id("user_pwd").send_keys("123456")

#通过定位密码框，enter回车来代替登录按钮
driver.find_element_by_id("user_pwd").send_keys(Keys.ENTER)
time.sleep(2)
'''#也可定位登陆按钮，通过 enter（回车）代替 click()
driver.find_element_by_id("login").send_keys(Keys.ENTER)'''

driver.quit()
