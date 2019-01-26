#！/usr/bin/env python
#_*_conding:utf-8_*_
# @Time    : 2019/1/26 0026 上午 11:04
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : login.py


from selenium import webdriver
import time


def login(driver, user, password):

    # 打开课堂派首页
    driver.get("https://w.ketangpai.com/pages/user/login.html")
    driver.implicitly_wait(10)
    # 输入账号
    driver.find_element_by_name("emailphone").send_keys(user)
    # 输入密码
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_xpath('//*[@class="log-btn fs32 active"]').click()

if __name__ == "__main__":
    driver = webdriver.Chrome()
    # 调用登录
    login(driver, "1402686685@qq.com", "zhang199217")
    print("登录成功")
