import unittest
import sys
import os
sys.path.append(os.getcwd()+r'\ranzhi')
from page.login_page import LoginPage
from base.util import BoxDriver,GetExcel,GetLogger
from time import sleep
from parameterized import parameterized
class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.logger=GetLogger('ranzhi/report/ranzhi.log')
        self.driver = BoxDriver(url='http://localhost/ranzhi/www/sys/user-login.html')
        self.logger.info('打开了登录页面！')
        self.loginPage = LoginPage(self.driver)


    @parameterized.expand(GetExcel().get(r'ranzhi\data\data.xlsx','login_success'))
    def test_login_success(self,uname,upwd):
        '''登陆成功功能测试用例'''
        try:
            self.loginPage.login(uname,upwd)
            self.logger.info('登陆成功！')
            #断言
            realname=self.loginPage.get_realname()
            self.assertEqual(realname,uname,'登录不成功！')
            self.logger.info('断言成功')
        except Exception as e:
            raise NameError('登录失败，代码错误！')
            print(e)
        finally:
            self.loginPage.logout()
            self.logger.debug('退出登录！')
    @parameterized.expand(GetExcel().get(r'ranzhi\data\data.xlsx','login_fail'))
    def test_login_fail(self,uname,upwd,ex_info):
        '''登陆失败功能测试用例'''
        #try里边的字句发生异常，不会再执行try里边发生异常后边的字句
        #finally:无论程序有没有异常报错，都会执行finally里边的字句
        try:
            self.loginPage.login(uname,upwd)
            self.logger.info('测试登录失败！')
            sleep(1)
            #断言
            info=self.loginPage.get_info()
            self.assertEqual(info,ex_info)
            self.logger.debug('断言成功！')
        except Exception as e:
            print(e)
            self.logger.info('代码发生异常！')
            raise NameError('登录失败，代码错误！')#抛异常后，Exception里边后边的代码不再执行
            
        finally:
            self.loginPage.confirm()
            self.logger.critical('点击确定按钮')

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()