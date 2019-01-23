#！/usr/bin/env python
#_*_conding:dtf-8_*_
# @Time    : 2019/1/14 0014 下午 17:32
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : sleep_time.py


from selenium import webdriver
import  time#调入time函数
browser=webdriver.Firefox()


browser.get("http://www.baidu.com")
time.sleep(0.3)#休眠0.3秒
browser.find_element_by_id("kw").send_keys("selenium")
browser.find_element_by_id("su").click()

time.sleep(3)#休眠3秒
browser.quit()





