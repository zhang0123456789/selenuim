#！/usr/bin/env python
#_*_conding:utf-8_*_
# @Time    : 2019/1/26 0026 下午 13:25
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : homework.py


'''作业：上传作业、作业留言、查看作业提交状态'''
from selenium import webdriver
import time


class HomeWork:

    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://w.ketangpai.com/pages/main/index.html")
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath('//*[@class="course-main-list"]').click()


    def upload_work(self):


