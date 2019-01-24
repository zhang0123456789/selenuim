#！/usr/bin/env python
#_*_conding:utf-8_*_
# @Time    : 2019/1/24 0024 上午 9:37
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : alert_confirm_prompt.py


'''二、alert操作
1.先用switch_to_alert()方法切换到alert弹出框上
2.可以用text方法获取弹出的文本 信息
3.accept()点击确认按钮
4.dismiss()相当于点右上角x，取消弹出框    （url的路径，直接复制浏览器打开的路径）'''
# from selenium import  webdriver
# import time
# driver=webdriver.Chrome()
# driver.get('D:\python_study\selenuim\窗口\\alert.html')
# time.sleep(4)
# driver.find_element_by_id("alert").click()
# time.sleep(3)
#
# t=driver.switch_to.alert
# #打印告警框文本内容
# print(t.text)
# #点击告警框按钮
# t.accept()
# #t.dismiss()相当于点x按钮，取消





#三、confirm操作
'''
1.先用switch_to_alert()方法切换到alert弹出框上
2.可以用text方法获取弹出的文本 信息
3.accept()点击确认按钮
4.dismiss()相当于点取消按钮或点右上角x，取消弹出框
（url的路径，直接复制浏览器打开的路径）'''
# from selenium import  webdriver
# import time
# driver=webdriver.Chrome()
# driver.get('D:\python_study\selenuim\窗口\\alert.html')
# time.sleep(4)
# driver.find_element_by_id("confirm").click()
# time.sleep(3)
# t=driver.switch_to.alert
# #打印告警框文本内容
# print(t.text)
# t.accept()







#四、prompt操作
'''
1.先用switch_to_alert()方法切换到alert弹出框上
2.可以用text方法获取弹出的文本 信息
3.accept()点击确认按钮
4.dismiss()相当于点右上角x，取消弹出框
5.send_keys()这里多个输入框，可以用send_keys()方法输入文本内容
（url的路径，直接复制浏览器打开的路径)'''
# from selenium import  webdriver
# import time
# driver=webdriver.Chrome()
# driver.get('D:\python_study\selenuim\窗口\\alert.html')
# time.sleep(4)
# driver.find_element_by_id("prompt").click()
# time.sleep(3)
# t=driver.switch_to.alert
# #打印告警框文本内容
# print(t.text)
# t.send_keys("hello selenium2")



#六、最终代码

# coding:utf-8

from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.select import Select

import time

driver = webdriver.Chrome()
url = "https://www.baidu.com"
driver.get(url)
driver.implicitly_wait(20)
# 鼠标移动到“设置”按钮
mouse = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(mouse).perform()
driver.find_element_by_link_text("搜索设置").click()
# 通过text:select_by_visible_text()
s = driver.find_element_by_id("nr")
Select(s).select_by_visible_text("每页显示20条")
time.sleep(3)
s.click()
driver.find_element_by_link_text("保存设置").click()
time.sleep(5)
# 获取alert弹框
t = driver.switch_to.alert
print (t.text)
t.accept()