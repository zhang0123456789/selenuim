#！/usr/bin/env python
#_*_conding:utf-8_*_
# @Time    : 2019/1/24 0024 上午 11:58
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : js处理内嵌div带有滚动条.py


'''二、纵向滚动
1.这个是div的属性：<div id="yoyoketang" name="yoyo" class="scroll">
2.这里最简单的通过id来定位，通过控制 scrollTop的值来控制滚动条高度
3.运行下面代码，观察页面是不是先滚动到底部，过五秒再回到顶部。（get里面地址是浏览器打开该页面的地址）'''
# from  selenium import webdriver
# import time
# driver=webdriver.Chrome()
# driver.get('D:\python_study\selenuim\js操作\div.html')
# #纵向底部
# js1='document.getElementById("yoyoketang").scrollTop=10000'
# driver.execute_script(js1)
# time.sleep(10)
# #纵向顶部
# js2='document.getElementById("yoyoketang").scrollTop=0'
# driver.execute_script(js2)






'''三、横向滚动
1.先通过id来定位，通过控制scrollLeft的值来控制滚动条高度'''
# from  selenium import webdriver
# import time
# driver=webdriver.Chrome()
# driver.get('D:\python_study\selenuim\js操作\div.html')
# #横向右侧
# js3='document.getElementById("yoyoketang").scrollLeft=10000'
# driver.execute_script(js3)
# time.sleep(10)
# #横向左侧
# js4='document.getElementById("yoyoketang").scrollLeft=0'
# driver.execute_script(js4)









'''四、用class属性定位
 1.js用class属性定位，返回的是一个list对象，这里取第一个就可以了。
2.这里要注意了，element和elements有很多小伙伴傻傻分不清楚。'''

from  selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get('D:\python_study\selenuim\js操作\div.html')
#获取的class返回的是list对象，取list的第一个
js5='document.getElementsByClassName("scroll")[0].scrollTop=10000'
driver.execute_script(js5)
time.sleep(10)
#控制横向滚动条位置
js6='document.getElementsByClassName("scroll")[0].scrollLeft=10000'
driver.execute_script(js6)