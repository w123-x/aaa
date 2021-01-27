from util import BoxDriver,BasePage,GetYaml
from time import sleep
import yaml

class LoginPage(BasePage):

    # def __init__(self):
    #     super().__init__(BoxDriver())

    # 默认的构造方法
    # def __init__(self,driver):
    #     super().__init__(driver)

    config = GetYaml().get(r'ranzhi\config.yaml')
    # 定位信息
    ACCOUNT = config['LoginPage']['ACCOUNT']
    PASSWORD = config['LoginPage']['PASSWORD']
    SUBMIT = config['LoginPage']['SUBMIT']

    def login(self,uname='admin',upwd='123456'):
        '''登陆Ranzhi系统'''    
        driver = self.driver

        # 用户名
        driver.input(self.ACCOUNT,uname)
        # 密码
        driver.input(self.PASSWORD,upwd)
        # 登陆
        driver.click(self.SUBMIT)

    def logout(self):
        '''签退'''
        self.driver.click('l 签退')
        sleep(1)

    def confirm(self):
        '''登陆失败时点击确定'''
        self.driver.click('x /html/body/div[2]/div/div/div[2]/button')
        sleep(1)
        
    def get_realname(self):
        '''登陆成功以后获取用户真名'''
        element = self.driver.find_element('x //*[@id="mainNavbar"]/div/ul[1]/li/a')
        return element.text

    def get_info(self):
        '''登陆失败以后获取提示信息'''
        element = self.driver.find_element('xpath /html/body/div[2]/div/div/div[1]/div')
        return element.text

if __name__ == "__main__":
    page = LoginPage(BoxDriver(url='http://localhost/ranzhi/www/sys/user-login.html'))
    page.login(uname='user1',upwd='123')
    print('info=',page.get_info())