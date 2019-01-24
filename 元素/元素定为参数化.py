#！/usr/bin/env python
#_*_conding:utf-8_*_
# @Time    : 2019/1/24 0024 下午 17:59
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : 元素定为参数化.py


'''一、find_element()
1.selenium元素定位里面其实是有这个方法的，只是大部分时候都是结合By方法使用'''
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# driver.get("http://www.baidu.com")
# driver.find_element(By.ID,"kw").send_keys("yoyoketang")





'''二、查看find_element方法源码'''
#1.find_element跟find_element_by_xxx到底有什么区别呢？好奇害死猫啊，找到这个路径：Lib\site-packages\selenium\webdriver\\remote\utils.py
#2.打开文件夹后发现，其实定find_element_by_xxx的方法都是返回的find_element方法，也就是说那八个定位方法其实就是八个小分支。




'''四、定位参数化
1.小编一直追求简单粗暴的方式，接下来就用最简单的方法去定位
2.总结下几种定位方法(字符串中间是空格需注意)
by_id= "id"
by_xpath = "xpath"
by_link_text = "link text"
by_partial_text = "partial link text"
by_name = "name"
by_tag_name = "tag name"
by_class_name = "class name"
by_css_selector = "css selector"'''


from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element("id","kw").send_keys("yoyoketang")
driver.find_element('css selector',"#su").click()

# t1 = driver.find_element("link text", "糯米").text
# print (t1)
# t2 = driver.find_element("name", "tj_trnews").text
# print (t2)
# t3 = driver.find_element("class name", "bri").text
# print （t3）