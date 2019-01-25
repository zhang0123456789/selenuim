#！/usr/bin/env python
#_*_conding:utf-8_*_
# @Time    : 2019/1/24 0024 下午 18:12
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : 某个元素截图.py



from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://www.baidu.com/')

driver.save_screenshot('button.png')
element = driver.find_element_by_id("su")
print(element.location)                # 打印元素坐标