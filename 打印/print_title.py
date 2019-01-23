#！/usr/bin/env python
#_*_conding:dtf-8_*_
# @Time    : 2019/1/14 0014 下午 17:58
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : print_title.py

'''虽然我没看到脚本的执行过程，但我在执行结果里看'''
'''百度一下，你就知道
说明页面正确被我打开'''
from  selenium import  webdriver
driver=webdriver.Chrome()

driver.get("http://www.baidu.com")
print( driver.title)#把页面上的title打印出来

driver.quit()