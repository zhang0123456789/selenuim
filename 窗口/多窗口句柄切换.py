#！/usr/bin/env python
#_*_conding:utf-8_*_
# @Time    : 2019/1/23 0023 下午 15:59
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : 多窗口句柄切换.py

'''有些页面的链接打开后，会重新打开一个窗口，对于这种情况，
想在新页面上操作，就得先切换窗口了。获取窗口的唯一标识用句柄表示，
所以只需要切换句柄，我们就能在多个页面上灵活自如的操作了。'''



#二、获取当前窗口句柄
'''
1.元素有属性，浏览器的窗口其实也有属性的，只是你看不到，浏览器窗口的属性用句柄（handle）来识别。
2.人为操作的话，可以通过眼睛看，识别不同的窗口点击切换。但是脚本没长眼睛，它不知道你要操作哪个窗口，这时候只能句柄来判断了。
3.获取当前页面的句柄：driver.current_window_handle'''
# from selenium import webdriver
# import time
# driver=webdriver.Chrome()
# driver.get("http://sz.ganji.com/")
# driver.implicitly_wait(10)
# #获取当前窗口句柄
# h=driver.current_window_handle
# print(h)


#三、获取所有句柄
''' 
1.定位赶集网招聘求职按钮，并点击
2.点击后，获取当前所以的句柄：window_handles'''

# from selenium import webdriver
# import time
# driver=webdriver.Chrome()
# driver.get("http://sz.ganji.com/")
# driver.implicitly_wait(10)
# h=driver.current_window_handle
# print(h)#获取首页窗口句柄
# driver.find_element_by_link_text("租房").click()
# all_h=driver.window_handles
# print(all_h)



#四、切换句柄
'''
方法一：
1.循环判断是否与首页句柄相等
2.如果不等，说明是新页面的句柄
3.获取的新页面句柄后，可以切换到新打开的页面上
4.打印新页面的title,看是否切换成功
方法二：
1.直接获取all_h这个list数据里面第二个hand的值：all_h[1]'''
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("http://sz.ganji.com/")
driver.implicitly_wait(10)
h=driver.current_window_handle
print(h)#获取首页窗口句柄
driver.find_element_by_link_text("租房").click()
all_h=driver.window_handles
print(all_h)
#方法一：判断句柄，不等于首页就切换
# for i in all_h:
#     if i !=h:
#         driver.switch_to.window(i)
#         print(driver.title)
#方法二：获取list里面第二个直接切换
driver.switch_to.window(all_h[1])
print(driver.title)

#关闭新窗口
driver.close()
#切换到首页句柄
driver.switch_to.window(h)
#打印当前的title
print(driver.title)