#！/usr/bin/env python
#_*_conding:dtf-8_*_
# @Time    : 2019/1/14 0014 下午 18:17
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : browser_style.py

'''
1.退出有两种方式，一种是close;另外一种是quit
2.close用于关闭当前窗口，当打开的窗口较多时，就可以用close关闭部分窗口
3.quit用于结束进程，关闭所有的窗口
4.最后结束测试，要用quit。quit可以回收c盘的临时文件'''
from selenium import webdriver
import time

browser=webdriver.Chrome()
#浏览器操作=webdriver.Ie()  #IE浏览器用这个
#浏览器操作=webdriver.Firefox()  #火狐浏览器用这个
browser.get("http://www.baidu.com")#打开百度
'''由于打开百度网址后，页面加载需要几秒钟，所以最好等到页面加载完成后再继续下一步操作'''
time.sleep(2) #设置等待时间，单位是秒（s）,时间值可以是小数也可以是整数

#参数数字为像素点
print("设置浏览器宽480、高800显示")
browser.set_window_size(480,800)
time.sleep(3)
browser.quit()
