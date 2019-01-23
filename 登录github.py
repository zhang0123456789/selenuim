#！/usr/bin/env python
#_*_conding:dtf-8_*_
# @Time    : 2019/1/22 0022 下午 17:16
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : 登录github.py

from selenium import webdriver
import time


def login(driver, user, password):
    '''登录github'''
    # 打开github首页
    driver.get("https://github.com/login")
    driver.implicitly_wait(10)
    # 输入账号
    driver.find_element_by_id("login_field").send_keys(user)
    # 输入密码
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_name("commit").click()

def logout(driver):
    '''退出github'''
    time.sleep(3)
    # 点右上角设置
    driver.find_element_by_xpath('//*[@class="HeaderNavlink name mt-1"]').click()
    time.sleep(1)
    # 点sign out
    driver.find_element_by_xpath('//*[@class="dropdown-item dropdown-signout"]').click()
    driver.quit()

if __name__ == "__main__":
    driver = webdriver.Chrome()
    # 调用登录
    login(driver, "zhang0123456789", "zhangqiuhua0123456789")
    print("hello  yoyo!")
    # 调用退出
    logout(driver)


