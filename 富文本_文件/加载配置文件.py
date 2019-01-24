#！/usr/bin/env python
#_*_conding:utf-8_*_
# @Time    : 2019/1/24 0024 上午 11:14
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : 加载配置文件.py


'''四、启动配置文件
1.由于文件路径存在字符：\ ，反斜杠在代码里是转义字符，这个有点代码基础的应该都知道。
不懂什么叫转义字符的，自己翻书补下基础吧！
2.遇到转义字符，为了不让转义，有两种处理方式：
第一种：\ (前面再加一个反斜杠)
第二种:r”\"（字符串前面加r，使用字符串原型)'''



from selenium import webdriver
#配置文件地址
profile_directory=r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\ulgboady.default'
#加载配置

profile = webdriver.FirefoxProfile(profile_directory)
# 启动浏览器配置
driver = webdriver.Firefox(profile)