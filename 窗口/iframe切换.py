#！/usr/bin/env python
#_*_conding:utf-8_*_
# @Time    : 2019/1/23 0023 下午 17:53
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : iframe切换.py



#三、切换iframe
'''
1.由于登录按钮是在iframe上，所以第一步需要把定位器切换到iframe上
2.用switch_to_frame方法切换，此处有id属性，可以直接用id定位切换'''
# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.get("http://mail.163.com/")
# driver.implicitly_wait(30)

#切换iframe
# driver.switch_to.frame("x-URS-iframe1548237893087.4248")
# driver.find_element_by_name("email").send_keys("18576437695")
# driver.find_element_by_name("password").send_keys("zhang199217")


#四、如果iframe没有id怎么办？
'''
1.这里iframe的切换是默认支持id和name的方法的，当然实际情况中会遇到没有id属性和name属性为空的情况，这时候就需要先定位iframe
2.定位元素还是之前的八种方法同样适用，这里我可以通过tag先定位到，也能达到同样效果'''
# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.get("http://mail.163.com/")
# driver.implicitly_wait(30)
# #切换iframe
# iframe=driver.find_element_by_tag_name('iframe')
# driver.switch_to.frame(iframe)
# # driver.switch_to.frame("x-URS-iframe1548237893087.4248")
# driver.find_element_by_name("email").send_keys("18576437695")
# driver.find_element_by_name("password").send_keys("zhang199217")



#五、释放iframe
'''
1.当iframe上的操作完后，想重新回到主页面上操作元素，这时候，就可以用switch_to_default_content()方法返回到主页面'''
# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.get("http://mail.163.com/")
# driver.implicitly_wait(30)
# driver.switch_to.frame("x-URS-iframe1548237893087.4248")
# driver.find_element_by_name("email").send_keys("18576437695")
# driver.find_element_by_name("password").send_keys("zhang199217")
# #释放iframe,重新回到主页面
# driver.switch_to.default_content()





#六、如何判断元素是否在iframe上？
'''
1.定位到元素后，切换到firepath界面
2.看firebug工具左上角，如果显示Top Window说明没有iframe
3.如果显示iframe#xxx这样的，说明在iframe上，#后面就是它的id'''





'''八、参考代码如下'''
from selenium import webdriver

driver = webdriver.Firefox()

driver.get("http://mail.163.com/")

driver.implicitly_wait(30)

# 切换iframe

# iframe = driver.find_element_by_tag_name("iframe")

# driver.switch_to_frame(iframe)

# driver.switch_to_frame("x-URS-iframe")

driver.switch_to.frame("x-URS-iframe")

driver.find_element_by_name("email").send_keys("123")

driver.find_element_by_name("password").send_keys("456")

# 释放iframe，重新回到主页面上

driver.switch_to.default_content()