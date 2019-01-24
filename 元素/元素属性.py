#！/usr/bin/env python
#_*_conding:utf-8_*_
# @Time    : 2019/1/24 0024 下午 16:52
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : 元素属性.py

'''一、获取页面title
1.有很多小伙伴都不知道title长在哪里，看下图左上角。
2.获取title方法很简单，直接driver.title就能获取到'''
# from selenium import webdriver
# import time
# driver=webdriver.Chrome()
# driver.implicitly_wait(10)
# driver.get("http://www.baidu.com")
# time.sleep(2)
# title=driver.title
# print(title)



'''二、获取元素的文本

1.如下图这种显示在页面上的文本信息，可以直接获取到
3.通过driver.text获取到文本'''
# from selenium import webdriver
# import time
# driver=webdriver.Chrome()
# driver.implicitly_wait(10)
# driver.get("http://www.baidu.com")
# time.sleep(2)
# title=driver.title
# print(title)
# text=driver.find_element_by_id("setf").text
# print(text)





'''三、获取元素的标签

1.获取百度输入框的标签属性'''
# from selenium import webdriver
# import time
# driver=webdriver.Chrome()
# driver.implicitly_wait(10)
# driver.get("http://www.baidu.com")
# time.sleep(2)
# title=driver.title
# print(title)
# text=driver.find_element_by_id("setf").text
# print(text)
# tag=driver.find_element_by_id("kw").tag_name
# print(tag)





'''四、获取元素的其它属性
1.获取其它属性方法:get_attribute("属性")，这里的参数可以是class、name等任意属性
2.如获取百度输入框的class属性'''
# from selenium import webdriver
# import time
# driver=webdriver.Chrome()
# driver.implicitly_wait(10)
# driver.get("http://www.baidu.com")
# time.sleep(2)
# title=driver.title
# print(title)
# text=driver.find_element_by_id("setf").text
# print(text)
# tag=driver.find_element_by_id("kw").tag_name
# print(tag)
# name=driver.find_element_by_id("kw").get_attribute("class")
# print(name)





'''五、获取输入框内的文本值
1、如果在百度输入框输入了内容，这里输入框的内容也是可以获取到的'''
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
time.sleep(2)
title=driver.title
print(title)
text=driver.find_element_by_id("setf").text
print(text)
tag=driver.find_element_by_id("kw").tag_name
print(tag)
name=driver.find_element_by_id("kw").get_attribute("class")
print(name)
driver.find_element_by_id("kw").send_keys("yoyoketang")
value=driver.find_element_by_id("kw").get_attribute("value")
print(value)
