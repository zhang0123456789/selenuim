#！/usr/bin/env python
#_*_conding:utf-8_*_
# @Time    : 2019/1/25 0025 下午 16:31
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : 浏览器提示语.py


from selenium import webdriver
#加启动配置
option=webdriver.ChromeOptions()
option.add_argument('disable-infobars')
#打开浏览器
driver=webdriver.Chrome(options=option)
driver.get("https://www.cnblogs.com/yoyoketang")
print(driver.title)