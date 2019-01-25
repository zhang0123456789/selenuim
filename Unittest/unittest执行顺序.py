#！/usr/bin/env python
#_*_conding:utf-8_*_
# @Time    : 2019/1/25 0025 上午 11:31
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : unittest执行顺序.py

from selenium import webdriver
import unittest,time

class Blog(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://passport.cnblogs.com/user/signin")
        self.driver.implicitly_wait(30)

    def login(self,username,psw):
        self.driver.find_element_by_id("input1").send_keys(username)
        self.driver.find_element_by_id("input2").send_keys(psw)
        self.driver.find_element_by_id("signin").click()
        time.sleep(3)

    def is_login_sucess(self):
        try:
            text=self.driver.find_element_by_id("lnk_current_user").text
            print(text)
            return True
        except:
            return False

    def test_01(self):
        u'''登录案例参考:账号，密码自己设置'''
        self.login(u"上海-悠悠", u"xxxx")#调用登录方法
        result=self.is_login_sucess()
        self.assertTrue(result)

    def test_02(self):
        u'''登录案例参考:账号，密码自己设置'''
        self.login(u"上海-悠悠", u"xxxx")  # 调用登录方法
        # 判断结果   # 交流QQ群：232607095
        result = self.is_login_sucess()
        self.assertTrue(result)


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
