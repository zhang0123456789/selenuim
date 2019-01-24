#！/usr/bin/env python
#_*_conding:utf-8_*_
# @Time    : 2019/1/24 0024 下午 17:32
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : 定为获取百度输入框的联想词.py


from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
time.sleep(3)
driver.find_element_by_id("kw").send_keys("博客")
#获取百度输入框的
time.sleep(2)
bd=driver.find_element_by_class_name("bdsug-overflow")
for i in bd:
    print (i.get_attribute("data-key"))

# 点击其中的一个，如：第二个
    if len(bd) > 1:
        bd[1].click()
        # 打印当前页面url
        print (driver.current_url)
    else:
        print ("未获取到匹配的词")