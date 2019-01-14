#！/usr/bin/env python
#_*_conding:dtf-8_*_
# @Time    : 2019/1/14 0014 下午 18:17
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : browser_style.py

from selenium import webdriver
import time
browser=webdriver.Chrome()
browser.get("http://www.baidu.com")
time.sleep(2)

#参数数字为像素点
print("设置浏览器宽480、高800显示")
browser.set_window_size(480,800)
time.sleep(3)
browser.quit()
