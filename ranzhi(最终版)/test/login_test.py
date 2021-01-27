import unittest,time
from page.login_page import LoginPage
from base.util import BoxDriver,GetExcel,GetCSV,GetLogger
from parameterized import parameterized

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.logger = GetLogger('ranzhi/report/ranzhi.log')
        self.driver = BoxDriver(url='http://localhost/ranzhi/www/sys/user-login.html')
        self.logger.info('打开了登陆页面！')
        self.loginPage = LoginPage(self.driver)

    @parameterized.expand(GetCSV().get(r'ranzhi\data\sample.csv'))
    def test_login_success(self,uname,upwd):
        '''登陆成功功能测试用例'''
        self.loginPage.login(uname,upwd)
        self.logger.info('登陆成功！')
        # 断言
        realname = self.loginPage.get_realname()
        # assert realname == 'admin'
        self.assertEqual(realname,uname,'登陆不成功！')
        self.logger.info('断言成功')
        # 错误是的例子
        # self.assertEqual(realname,uname1,'登陆不成功！')
        self.loginPage.logout()
        self.logger.debug('退出登陆')

    @parameterized.expand(GetExcel().get(r'ranzhi\data\data.xlsx','login_fail'))
    def test_login_fail(self,uname,upwd,ex_info):
        '''登陆失败功能测试用例'''
        try:
            self.loginPage.login(uname,upwd)
            self.logger.info('测试登陆失败')
            # 断言
            self.driver.wait(1)
            info = self.loginPage.get_info()
            self.assertEqual(info,ex_info)
            self.logger.debug('断言成功')
            # 出错时的例子
            # self.assertEqual(info,ex_info1)
        except Exception as e:
            self.logger.info('代码发生异常！')
            raise NameError('登陆失败，代码错误！')
        finally:
            self.loginPage.confirm()
            self.logger.critical('点击确定按钮')

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()