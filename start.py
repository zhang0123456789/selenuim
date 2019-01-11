#！/usr/bin/env python
#_*_conding:dtf-8_*_
# @Time    : 2019/1/11 0011 下午 17:50
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : start.py
from selenium import webdriver  #把包导入进来
browser=webdriver.Firefox()  #需要操控哪个浏览器

browser.get("http://www.baidu.com")#

browser.find_element_by_id('kw').send_keys('selenium2')#一个控件有若干属性id，name，百度的输入框的id叫kw,我要在输入框输入selenium

browser.find_element_by_id('su').click()#搜索的按钮的id叫su,我需要点一下按钮click()

browser.quit()#  退出并关闭窗口的每一个相关驱动程序

browser.close()#关闭当前窗口

