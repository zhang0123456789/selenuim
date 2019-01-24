#！/usr/bin/env python
#_*_conding:utf-8_*_
# @Time    : 2019/1/24 0024 下午 16:22
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : 显性等待.py

'''
在脚本中加入太多的sleep后会影响脚本的执行速度，虽然implicitly_wait()这种方法隐式等待方法一定程度上节省了很多时间。
但是一旦页面上某些js无法加载出来（其实界面元素经出来了），左上角那个图标一直转圈，这时候会一直等待的。'''



'''一、参数解释

1.这里主要有三个参数：
class WebDriverWait(object):driver, timeout, poll_frequency
2.driver:返回浏览器的一个实例，这个不用多说
3.timeout：超时的总时长
4.poll_frequency：循环去查询的间隙时间，默认0.5秒'''



'''二、元素出现：until()
1.until里面有个lambda函数，这个语法看python文档吧
2.以百度输入框为例'''
# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
#
# driver=webdriver.Chrome()
# driver.get("http://www.baidu.com")
# #等待时长为10秒，默认0.5秒询问一次
# WebDriverWait(driver,10).until(lambda x:x.find_element_by_id("kw")).send_keys("yoyo")



'''三、元素消失：until_not（）
1.判断元素是否消失，是返回Ture,否返回False
备注：此方法未调好，暂时放这'''
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
#等待时长为10秒，默认0.5秒询问一次
WebDriverWait(driver,10).until(lambda x:x.find_element_by_id("kw")).send_keys("yoyo")
#判断id为kw元素是否消失
is_disappeared = WebDriverWait(driver, 10, 1).\
    until_not(lambda x: x.find_element_by_id("kw").is_displayed())
print (is_disappeared)