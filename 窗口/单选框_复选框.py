#！/usr/bin/env python
#_*_conding:utf-8_*_
# @Time    : 2019/1/24 0024 上午 10:39
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : 单选框_复选框.py


'''三、单选：radio
 1.首先是定位选择框的位置
 2.定位id，点击图标就可以了，代码如下（获取url地址方法：把上面源码粘贴到文本保存为.html后缀后用浏览器打开，在浏览器url地址栏复制出地址就可以了）
  3.先点击boy后，等十秒再点击girl，观察页面变化'''
# from selenium import webdriver
# import time
# driver=webdriver.Chrome()
# driver.get('D:\python_study\selenuim\窗口\\checkbox.html')
# driver.find_element_by_id('boy').click()



#四、复选框：checkbox
'''
1.勾选单个框，比如勾选selenium这个，可以根据它的id=c1直接定位到点击就可以了'''
# from selenium import webdriver
# import time
# driver=webdriver.Chrome()
# driver.get('D:\python_study\selenuim\窗口\\checkbox.html')
# driver.find_element_by_id('c2').click()


#五、复选框：checkbox
'''
1、全部勾选，可以用到定位一组元素，从上面源码可以看出，复选框的type=checkbox,这里可以用xpath语法：.//*[@type='checkbox']
2、这里注意，敲黑板做笔记了：find_elements是不能直接点击的，它是复数的，所以只能先获取到所有的checkbox对象，然后通过for循环去一个个点击操作'''
# from selenium import webdriver
# import time
# driver=webdriver.Chrome()
# driver.get('D:\python_study\selenuim\窗口\\checkbox.html')
# checkboxes=driver.find_elements_by_xpath('//*[@type="checkbox"]')
# for i in checkboxes:
#     i.click()



#六、判断是否选中：is_selected()
'''
1.有时候这个选项框，本身就是选中状态，如果我再点击一下，它就反选了，这可不是我期望的结果，那么可不可以当它是没选中的时候，
我去点击下；当它已经是选中状态，我就不点击呢？那么问题来了：如何判断选项框是选中状态？
2.判断元素是否选中这一步才是本文的核心内容，点击选项框对于大家来说没什么难度。获取元素是否为选中状态，打印结果如下图。
3.返回结果为bool类型，没点击时候返回False,点击后返回True，接下来就很容易判断了，既可以作为操作前的判断，也可以作为测试结果的判断'''
#
# from selenium import webdriver
# import time
# driver=webdriver.Chrome()
# driver.get('D:\python_study\selenuim\窗口\\checkbox.html')
# #没点击操作前，判断选项框状态
# s=driver.find_element_by_id("boy").is_selected()
# print(s)
# driver.find_element_by_id("boy").click()
# #点击后，判断元素是否为选中状态
# r=driver.find_element_by_id("boy").is_selected()
# print(r)



#七、参考代码：
# coding:utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('D:\python_study\selenuim\窗口\\checkbox.html')
# 没点击操作前，判断选项框状态
s = driver.find_element_by_id("boy").is_selected()
print (s)
time.sleep(5)

driver.find_element_by_id("boy").click()
# 点击后，判断元素是否为选中状态
r = driver.find_element_by_id("boy").is_selected()
print (r)
time.sleep(5)

# 复选框单选
driver.find_element_by_id("c1").click()
time.sleep(5)
# 复选框全选
checkboxs = driver.find_elements_by_xpath(".//*[@type='checkbox']")
for i in checkboxs:
    i.click()