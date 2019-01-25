#！/usr/bin/env python
#_*_conding:dtf-8_*_
# @Time    : 2019/1/22 0022 下午 15:00
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : windows截屏.py

'''1.打开网站之后，也可以对屏幕截屏
2.截屏后设置制定的保存路径+文件名称+后缀'''
from  selenium import  webdriver
import time

driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
time.sleep(3)
driver.get_screenshot_as_file("D:\\python_study\\selenuim\\b1.png")
time.sleep(3)
driver.quit()