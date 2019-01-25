#！/usr/bin/env python
#_*_conding:utf-8_*_
# @Time    : 2019/1/25 0025 上午 11:21
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : unittest登录.py

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time,unittest

class Blog(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http://www.cnblogs.com/yoyoketang")

    def test_blog(self):
        time.sleep(3)
        result=EC.title_is('上海-悠悠 - 博客园')(self.driver)
        print(result)
        self.assertTrue(result)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
