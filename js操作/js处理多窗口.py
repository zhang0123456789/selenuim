#！/usr/bin/env python
#_*_conding:utf-8_*_
# @Time    : 2019/1/24 0024 下午 13:57
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : js处理多窗口.py


'''在打开页面上链接的时候，经常会弹出另外一个窗口,这样在多个窗口之间来回切换比较复杂，
那么有没有办法让新打开的链接在一个窗口打开呢？
要解决这个问题，得从html源码上找到原因，然后修改元素属性才能解决。
很显然js在这方面是万能的，于是本篇得依靠万能的js大哥了。'''


'''一、多窗口情况
1.在打baidu的网站链接时，会重新打开一个窗口'''


'''二、查看元素属性：target="_blank"
1.查看元素属性，会发现这些链接有个共同属性：target="_blank"'''


'''三、去掉target="_blank"属性
1.因为此链接元素target="_blank"，所以打开链接的时候会重新打开一个标签页，那么解决这个问题，去掉该属性就可以了。
2.为了验证这个问题，可以切换到html编辑界面，手动去掉“_blank”属性
3.删除“_blank”属性后，重新打开链接，这时候会发现打开的新链接会在原标签页打开。'''



'''四、js去掉target="_blank"属性
1.第一步为了先登录，我这里加载配置文件免登录了（不会的看这篇：Selenium2+python自动化18-加载Firefox配置）
2.这里用到js的定位方法，定位该元素的class属性
3.定位到该元素后直接修改target属性值为空'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

profile_directory=r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\ulgboady.default'
profile=webdriver.FirefoxProfile(profile_directory)
driver=webdriver.Firefox(profile)

driver.get("https://www.baidu.com")

#修改元素的target属性
js = 'document.getElementsByClassName("mnav")[0].target="";'
driver.execute_script(js)
driver.find_element_by_link_text("地图").click()
