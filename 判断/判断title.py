#！/usr/bin/env python
#_*_conding:utf-8_*_
# @Time    : 2019/1/24 0024 下午 15:32
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : 判断title.py


'''一、源码分析

1.首先看下源码,如下
class title_is(object):
    """An expectation for checking the title of a page.
    title is the expected title, which must be an exact match
    returns True if the title matches, false otherwise."""'''

'''翻译：检查页面的title与期望值是都完全一致，如果完全一致，返回Ture,否则返回Flase
    def __init__(self, title):
        self.title = title
    def __call__(self, driver):
        return self.title == driver.title
2.注释翻译：检查页面的title与期望值是都完全一致，如果完全一致，返回True,否则返回Flase
3.title_is()这个是一个class类型，里面有两个方法
4.__init__是初始化内容，参数是title，必填项
5.__call__是把实例变成一个对象，参数是driver，返回的是self.title == driver.title，布尔值'''


'''二、判断title:title_is()
1.首先导入expected_conditions模块
2.由于这个模块名称比较长，所以为了后续的调用方便，重新命名为EC了（有点像数据库里面多表查询时候重命名）
3.打开博客首页后判断title,返回结果是True或False'''
# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as EC
# driver=webdriver.Chrome()
# driver.get("https://www.cnblogs.com/mimistudy/")
#
# title=EC.title_is(u'zhang0123456789-博客园')
# print(title(driver))




'''三、判断title包含:title_contains
1.这个类跟上面那个类差不多，只是这个是部分匹配（类似于xpath里面的contains语法）
2.判断title包含'上海-悠悠'字符串'''
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome()
driver.get("https://www.cnblogs.com/mimistudy/")
#判断title完全等于
title=EC.title_is(u'zhang0123456789-博客园')
print(title(driver))
#判断title包含
title1=EC.title_contains('zhang0123456789')
print(title1(driver))
#另一种写法
r1=EC.title_is(u'zhang0123456789-博客园')(driver)
r2=EC.title_contains('zhang0123456789')(driver)
print(r1)
print(r2)





#四、参考代码

# coding:utf-8
# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Firefox()
# driver.get("http://www.cnblogs.com/yoyoketang")
# # 判断title完全等于
# title = EC.title_is(u'上海-悠悠 - 博客园')
# print (title(driver))
#
# # 判断title包含
# title1 = EC.title_contains(u'上海-悠悠')
# print (title1(driver))
#
# # 另外一种写法,交流QQ群：232607095
# r1 = EC.title_is(u'上海-悠悠 - 博客园')(driver)
# r2 = EC.title_contains(u'上海-悠悠')(driver)
# print (r1)
# print (r2)