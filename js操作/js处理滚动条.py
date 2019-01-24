#！/usr/bin/env python
#_*_conding:utf-8_*_
# @Time    : 2019/1/24 0024 上午 10:19
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : js处理滚动条.py


'''二、控制滚动条高度

1.滚动条回到顶部：
js="var q=document.getElementById('id').scrollTop=0"
driver.execute_script(js）
2.滚动条拉到底部
js="var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
3.这里可以修改scrollTop 的值，来定位右侧滚动条的位置，0是最上面，10000是最底部。'''




#三、横向滚动条
'''
1.有时候浏览器页面需要左右滚动（一般屏幕最大化后，左右滚动的情况已经很少见了）。
2.通过左边控制横向和纵向滚动条scrollTo(x, y）js = "window.scrollTo(100,400);"
driver.execute_script(js)
3.第一个参数x是横向距离，第二个参数y是纵向距离'''




#五、元素聚焦
'''
1.虽然用上面的方法可以解决拖动滚动条的位置问题，但是有时候无法确定我需要操作的元素
在什么位置，有可能每次打开的页面不一样，元素所在的位置也不一样，怎么办呢？
2.这个时候我们可以先让页面直接跳到元素出现的位置，然后就可以操作了。同样需要借助JS去实现。 
3.元素聚焦：
target = driver.find_element_by_xxxx()
driver.execute_script("arguments[0].scrollIntoView();", target)'''



#六、获取浏览器名称:driver.name
'''
1.为了解决不同浏览器操作方法不一样的问题，可以写个函数去做兼容。
2.先用driver.name获取浏览器名称，然后用if语句做个判断'''
from  selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
print(driver.name)



'''七、兼容性
1.兼容谷歌和firefox/IE'''
#回到顶部
# def scroll_top():
#     if driver.name=="chrome":
#         js="var q=document.body.scrollTop=0"
#     else:
#         js="var q=document.documentElement.scrollTop=0"
#     return driver.execute_script(js)
# #拉倒底部
# def scroll_foot():
#     if driver.name=="chrome":
#         js = "var q=document.body.scrollTop=10000"
#     else:
#         js = "var q=document.documentElement.scrollTop=10000"
#     return driver.execute_script(js)



'''
#滚动到底部
js = "window.scrollTo(0,document.body.scrollHeight)" 
driver.execute_script(js)
#滚动到顶部
js = "window.scrollTo(0,0)" 
driver.execute_script(js)
'''


#九、参考代码如下：
# coding:utf-8
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
print (driver.name)
## 回到顶部
#def scroll_top():
#     if driver.name == "chrome":
#        js = "var q=document.body.scrollTop=0"
#     else:
#         js = "var q=document.documentElement.scrollTop=0"
#     return driver.execute_script(js)
# 拉到底部
#def scroll_foot():
#    if driver.name == "chrome":
#         js = "var q=document.body.scrollTop=10000"
#     else:
#         js = "var q=document.documentElement.scrollTop=10000"
#     return driver.execute_script(js)

#滚动到底部
js = "window.scrollTo(0,document.body.scrollHeight)"
driver.execute_script(js)

#滚动到顶部
js = "window.scrollTo(0,0)"
driver.execute_script(js)


# 聚焦元素
# target = driver.find_element_by_xxxx()
# driver.execute_script("arguments[0].scrollIntoView();", target)