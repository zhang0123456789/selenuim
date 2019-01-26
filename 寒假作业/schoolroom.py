#！/usr/bin/env python
#_*_conding:utf-8_*_
# @Time    : 2019/1/26 0026 上午 11:27
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : schoolroom.py


'''课堂：加入班级、退课、进入班级'''
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
import time,unittest


class SchoolRoom:

    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://w.ketangpai.com/pages/main/index.html")
        self.driver.implicitly_wait(30)
        # 输入账号


    def test_add_class(self):
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@class="fs30 c-btn banji"]').click()
        self.driver.find_element_by_xpath('//*[@class="fs26"]//following-sibling::div').send_keys('29942D')
        locator = ('class', 'fs36 text-overflow')
        text = 'python-WEB实战考核项目'
        result= EC.text_to_be_present_in_element_value(locator, text)(self.driver)
        print(result)



    def test_leave_class(self):
        time.sleep(3)
        self.driver.find_elements_by_xpath('//*[@class="course-main-list"]//span[1]').click()
        self.driver.find_element_by_id('quitClass').click()
        time.time(5)
        self.driver.find_element_by_class_name('btn sure').click()



    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()


