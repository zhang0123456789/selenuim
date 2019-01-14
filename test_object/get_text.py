#！/usr/bin/env python
#_*_conding:dtf-8_*_
# @Time    : 2019/1/14 0014 下午 18:39
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : get_text.py

'''text 用于获取元素的文'''

'''下面把百度首页底部的声明打印'''
from  selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
time.sleep(2)


#id =cp元素的文本信息
data=driver.find_element_by_id("cp").text
print(data)
time.sleep(3)

driver.quit()