#！/usr/bin/env python
#_*_conding:utf-8_*_
# @Time    : 2019/1/25 0025 上午 10:54
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : 判断文本.py


'''二、判断文本,如果判断成功，就返回True
1.判断百度首页上，“学术”按钮这个元素中存在文本：学术
2.locator参数是定位的方法
3.text参数是期望的值'''
# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as EC
# driver=webdriver.Chrome()
# driver.get("https://www.baidu.com")
# locator=('name','tj_trxueshu')
# text='学术'
# result=EC.text_to_be_present_in_element(locator,text)(driver)
# print(result)


'''1.如果判断失败，就返回False'''
# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as EC
# driver=webdriver.Chrome()
# driver.get("https://www.baidu.com")
# locator=('name','tj_trxueshu')
# text1='学术网'
# result1=EC.text_to_be_present_in_element(locator,text1)(driver)
# print(result1)




from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome()
driver.get("https://www.baidu.com")
locator=('id','su')
text2='百度一下'
result2=EC.text_to_be_present_in_element_value(locator,text2)(driver)
print(result2)
