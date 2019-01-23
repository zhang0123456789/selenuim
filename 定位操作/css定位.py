#！/usr/bin/env python
#_*_conding:dtf-8_*_
# @Time    : 2019/1/22 0022 下午 16:16
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : css定位.py

'''
3.css用#号表示id属性,如：#kw
4.css用.表示class属性，如：.s_ipt
5.css直接用标签名称，无任何标示符，如：input'''

from selenium import webdriver

browser=webdriver.Chrome()
browser.get("http://www.baidu.com")
'''一、css:属性定位'''
#css通过id属性定位
browser.find_element_by_css_selector("#kw").send_keys('selenium')
#css通过class属性定位
browser.find_element_by_css_selector(".s_ipt").send_keys('selenium')
#css通过标签属性定位
browser.find_element_by_css_selector("input").send_keys('selenium')

'''二、css:其它属性'''
#css通过name属性定位
browser.find_element_by_css_selector("[name='wd]").send_keys('selenium')
#css通过autocomplete定位
browser.find_element_by_css_selector("[autocomplete='of']").send_keys('selenium')
#css通过type属性定位
browser.find_element_by_css_selector("[type='text']").send_keys('selenium')


'''css页可以通过标签与属性的组合来定位元素'''
#css通过标签与class属性的组合定位
browser.find_element_by_css_selector("input.s_ipt").send_keys('selenium')
#css通过标签与id属性的组合定位
browser.find_element_by_css_selector("input#kw").send_keys('selenium')
#css通过标签与其他属性组合定位
browser.find_element_by_css_selector("input[id='kw']").send_keys('selenium')

'''四、css:层级关系
1.在前面一篇xpath中讲到层级关系定位，这里css也可以达到同样的效果
2.如xpath：//form[@id='form']/span/input和
//form[@class='fm']/span/input也可以用css实现'''
browser.find_element_by_css_selector("form#form>span>input").send_keys('selenium')
browser.find_element_by_css_selector("form.fm>span>input")