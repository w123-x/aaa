from page.login_page import LoginPage
from page.adduser_page import AddUserPage
from base.util import BoxDriver

class AddUserTest:

    def adduser_test(self):
        driver = BoxDriver()
        # loginPage = LoginPage(driver)
        # loginPage.login()
        adduserPage = AddUserPage(driver)
        adduserPage.login()
        adduserPage.add_user()

if __name__ == "__main__":
    AddUserTest().adduser_test()

