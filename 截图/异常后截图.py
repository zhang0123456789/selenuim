#！/usr/bin/env python
#_*_conding:utf-8_*_
# @Time    : 2019/1/25 0025 下午 16:35
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : 异常后截图.py


'''一、windows截图方法
1.get_screenshot_as_file(self, filename)
--这个方法是获取当前window的截图，出现IOError时候返回False,截图成功返回True。
filename参数是保存文件的路径。
Usage:driver.get_screenshot_as_file('/Screenshots/foo.png')
2.get_screenshot_as_base64(self)
--这个方法也是获取屏幕截图，保存的是base64的编码格式，在HTML界面输出截图的时候，会用到。
比如，想把截图放到html测试报告里。
Usage:driver.get_screenshot_as_base64()
3.get_screenshot_as_png(self)
--这个是获取屏幕截图，保存的是二进制数据，很少用到.
Usage:driver.get_screenshot_as_png()'''




'''二、异常后截图
1.为了能抛异常，把定位登录按钮的id换了个错的id。
2.给图片命名时候加个时间戳，避免同一个文件名称被覆盖掉。
3.文件路径，这里直接写的文件名称，就是跟当前的脚本同一个路径。如果图片输出到其它文件路径，需要些文件的绝对路径了。
4.截图的结果，如果没截到图返回False,截图成功会返回True。'''
# from selenium import webdriver
# import time
# url_login="https://passport.cnblogs.com/user/signin"
# driver=webdriver.Chrome()
# driver.get(url_login)
# try:
#     driver.find_element_by_id("input1").send_keys("上海-悠悠")
#     driver.find_element_by_id("input2").send_keys("对对对")
#     #登录id是错的，定位会抛出异常
#     driver.find_element_by_id("signin1").click()
# except Exception as msg:
#     print("异常原因%s"%msg)
#     #图片名称可以加时间戳
#     nowTime=time.strftime("%Y%m%d.%H.%M.%S")
#     t=driver.get_screenshot_as_file('%s.png'%nowTime)
#     print("截图结果：%s"%t)



'''三、selenium实例
1.在unittest框架里写用例的时候，我们希望在断言失败的时候，对当前屏幕截图。
2.如果加try...except捕获异常后结果，此时所有的测试用例都是通过的了，会影响测试结果。解决办法其实很简单，再把异常抛出来就行了。'''

from selenium import webdriver
import time,unittest
from selenium.webdriver.support import expected_conditions as EC
class Login(unittest.TestCase):
    def setUp(self):
        url_login = "https://passport.cnblogs.com/user/signin"
        self.driver = webdriver.Firefox()
        self.driver.get(url_login)

    def test_01(self):
        '''前面输入账号密码，让正确运行到assert这一步，断言故意设置为False不成功'''
        try:
            self.driver.find_element_by_id("input1").send_keys("zhang0123456789")
            self.driver.find_element_by_id("input2").send_keys("@zhang0123456789")
            # 登录id是错的，定位会抛异常
            self.driver.find_element_by_id("signin").click()
            # 　判断登录成功页面是否有账号："上海-悠悠"
            time.sleep(3)
            locator = ("id", "lnk_current_user")
            result = EC.text_to_be_present_in_element(locator, "zhang0123456789")(self.driver)
            self.assertFalse(result)
        except Exception as msg:
            print(u"异常原因%s" % msg)
            # 图片名称可以加个时间戳
            nowTime = time.strftime("%Y%m%d.%H.%M.%S")
            self.driver.get_screenshot_as_file('%s.png' % nowTime)
            raise

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()