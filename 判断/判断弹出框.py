#！/usr/bin/env python
#_*_conding:utf-8_*_
# @Time    : 2019/1/24 0024 下午 16:03
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : 判断弹出框.py

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from  selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome()
driver.get( "https://www.baidu.com")
mouse = WebDriverWait(driver, 10).until(lambda x: x.find_element("link text", "设置"))
ActionChains(driver).move_to_element(mouse).perform()
WebDriverWait(driver,10).until(lambda x: x.find_element("link text", "搜索设置")).click()
#选择设置项
s=WebDriverWait(driver,10).until(lambda x: x.find_element("id", "nr"))
Select(s).select_by_visible_text("每页显示50条")
#点保存按钮
js = 'document.getElementsByClassName("prefpanelgo")[0].click();'
driver.execute_script(js)
# 判断弹窗结果
result = EC.alert_is_present()(driver)
if result:
    print (result.text)
    result.accept()
else:
    print ("alert 未弹出！")