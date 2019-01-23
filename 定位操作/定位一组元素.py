#！/usr/bin/env python
#_*_conding:utf-8_*_
# @Time    : 2019/1/23 0023 下午 15:09
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : 定位一组元素.py

'''有时候一个页面上有多个对象需要操作，如果一个个去定位的话，比较繁琐，
这时候就可以定位一组对象 ,webdriver 提供了定位一组元素的方法，
跟前面八种定位方式其实一样，只是前面是单数，这里是复数形式：find_elements '''
from selenium import webdriver
# '''定位搜索结果'''
# driver=webdriver.Chrome()
# driver.get("http://www.baidu.com")
# driver.implicitly_wait(10)
# driver.find_element_by_id("kw").send_keys("测试部落")
# driver.find_element_by_id("kw").submit()
# s=driver.find_elements_by_xpath('//*[@class="t"]/a')
# '''确认定位结果  用for循环  这里可以获取href属性，打印出url地址'''
# for i in s:
#     print(i.get_attribute("href"))




from selenium import webdriver
import  random
'''定位搜索结果'''
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.implicitly_wait(10)
driver.find_element_by_id("kw").send_keys("测试部落")
driver.find_element_by_id("kw").submit()#用的submit的方法，submit相当于回车键
s=driver.find_elements_by_xpath('//*[@class="t"]/a')
#设置随机值
t=random.randint(0,9)
print(t)

#随机取一个结果点击鼠标
s[t].click()
