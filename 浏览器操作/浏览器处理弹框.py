#！/usr/bin/env python
#_*_conding:utf-8_*_
# @Time    : 2019/1/24 0024 下午 17:52
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : 浏览器处理弹框.py


'''一、alert弹窗
accept - 点击【确认】按钮
dismiss - 点击【取消】按钮（如有按钮）
send_keys - 输入内容（如有输入框）'''
# from selenium import webdriver
# import time
#
# driver = webdriver.Firefox()
# driver.get("http://www.runoob.com/try/try.php?filename=tryjs_alert")
# driver.switch_to.frame("iframeResult")
# driver.find_element_by_xpath("html/body/input").click()
# time.sleep(1)
# al = driver.switch_to.alert
# time.sleep(1)
# al.accept()







'''由于alert弹窗不美观，现在大多数网站都会使用自定义弹窗，使用Selenium自带的方法就驾驭不了了，此时就要搬出JS大法'''
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://sh.xsjedu.org/")
time.sleep(1)
js = 'document.getElementById("doyoo_monitor").style.display="none";'
driver.execute_script(js)