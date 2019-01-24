#！/usr/bin/env python
#_*_conding:utf-8_*_
# @Time    : 2019/1/24 0024 下午 16:30
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : js处理click失效问题.py


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Firefox()
url = "https://www.baidu.com"
driver.get(url)
time.sleep(3)
mouse = driver.find_element("link text", "设置")
ActionChains(driver).move_to_element(mouse).perform()
time.sleep(3)
driver.find_element("link text", "搜索设置").click()
time.sleep(3)
s = driver.find_element("id", "nr")
Select(s).select_by_visible_text("每页显示50条")

# 方法一：先点父元素 交流QQ群：232607095
# driver.find_element("id", "gxszButton").click()
# driver.find_element("class name", "prefpanelgo").click()

# 方法二：用js直接去点击 交流QQ群：232607095
js = 'document.getElementsByClassName("prefpanelgo")[0].click();'
driver.execute_script(js)