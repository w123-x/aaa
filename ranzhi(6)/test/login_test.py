import unittest,time
from page.login_page import LoginPage
from base.util import BoxDriver,GetExcel,GetCSV
from parameterized import parameterized

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = BoxDriver(url='http://localhost/ranzhi/www/sys/user-login.html')
        self.loginPage = LoginPage(self.driver)

    @parameterized.expand(GetCSV().get(r'ranzhi\data\sample.csv'))
    def test_login_success(self,uname,upwd):
        '''登陆成功功能测试用例'''
        self.loginPage.login(uname,upwd)
        # 断言
        realname = self.loginPage.get_realname()
        # assert realname == 'admin'
        self.assertEqual(realname,uname,'登陆不成功！')
        self.loginPage.logout()

    @parameterized.expand(GetExcel().get(r'ranzhi\data\data.xlsx','login_fail'))
    def test_login_fail(self,uname,upwd,ex_info):
        '''登陆失败功能测试用例'''
        self.loginPage.login(uname,upwd)
        # 断言
        self.driver.wait(1)
        info = self.loginPage.get_info()
        self.assertEqual(info,ex_info)
        self.loginPage.confirm()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()