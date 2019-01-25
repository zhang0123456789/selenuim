#！/usr/bin/env python
#_*_conding:utf-8_*_
# @Time    : 2019/1/25 0025 下午 16:22
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : 浏览器静默模式启动.py

'''实现静默模式启动浏览器完成自动化测试，这个模式是极好的，不需要占用电脑的屏幕。'''
from selenium import webdriver



'''
1.启动浏览器的时候不想看的浏览器运行，那就加载浏览器的静默模式，让它在后台偷偷运行。
2.通过对比发现，启动静默模式后，运行代码启动浏览器的速度更快了。'''
option=webdriver.ChromeOptions()
option.add_argument('headless')#静默模式

#打开charom浏览器
#driver=webdriver.Chrome(chrome_options=option)#警告内容，是chrome_options已经被弃用；使用options来代替chrome_options
driver=webdriver.Chrome(options=option)
driver.get("https://www.cnblogs.com/yoyoketang")
print(driver.title)