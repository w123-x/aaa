import unittest,time
from login_page import LoginPage
from util import BoxDriver
from parameterized import parameterized

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = BoxDriver(url='http://localhost/ranzhi/www/sys/user-login.html')
        self.loginPage = LoginPage(self.driver)

    @parameterized.expand([('admin','123456'),('user0','123456')])
    def test_login_success(self,uname,upwd):
        '''登陆成功功能测试用例'''
        self.loginPage.login(uname,upwd)
        # 断言
        realname = self.loginPage.get_realname()
        # assert realname == 'admin'
        self.assertEqual(realname,uname,'登陆不成功！')
        self.loginPage.logout()

    def test_login_fail(self):
        '''登陆失败功能测试用例'''
        self.loginPage.login(uname='admin',upwd='123')
        self.loginPage.confirm()
        self.loginPage.login(uname='tom',upwd='123')
        self.loginPage.confirm()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()