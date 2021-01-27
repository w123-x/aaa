import unittest,time
import os,sys
#sys.path.append(x)#将x所在的目录加入到搜索目录中
sys.path.append(os.getcwd()+r'\ranzhi')
from page.login_page import LoginPage
from page.adduser_page import AddUserPage
from base.util import BoxDriver,GetExcel,GetCSV
from parameterized import parameterized
from time import sleep
class AddUserTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = BoxDriver(url='http://localhost/ranzhi/www/sys/user-login.html')
        self.addUserPage = AddUserPage(self.driver)
        self.addUserPage.login()
        # 点击后台管理
        self.driver.click('id s-menu-superadmin')
        # # 进入iframe
        self.driver.switch_to_frame('id iframe-superadmin')
        self.driver.click('x //*[@id="shortcutBox"]/div/div[1]/div/a')
        
    @parameterized.expand(GetExcel().get(r'ranzhi\data\userdata.xlsx','Sheet1'))
    def test_add_user(self,account,realname,gender,dept,role,password1,password2,email):
        try:
            print('进入方法')
            self.addUserPage.add_user(account,realname,gender,dept,role,password1,password2,email)
            print('321332131')
        except Exception as e:
            print(e)
        finally:
            self.driver.click('l 添加成员')
if __name__ == "__main__":
    unittest.main()

