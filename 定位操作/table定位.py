#！/usr/bin/env python
#_*_conding:utf-8_*_
# @Time    : 2019/1/24 0024 下午 14:41
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : table定位.py


'''二、table特征
1.table页面查看源码一般有这几个明显的标签：table、tr、th、td
2.<table>标示一个表格
3.<tr>标示这个表格中间的一个行
4.</th> 定义表头单元格
5.</td> 定义单元格标签，一组<td>标签将将建立一个单元格，<td>标签必须放在<tr>标签内'''
from selenium import webdriver
driver=webdriver.Chrome()
driver.get('D:\python_study\selenuim\定位操作\\table.html')
t=driver.find_element_by_xpath("//*[@id='myTable']/tbody/tr[2]/td[1]")
print(t.text)