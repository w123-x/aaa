
from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
import random
import os,sys
#sys.path.append(x)#将x所在的目录加入到搜索目录中
sys.path.append(os.getcwd()+r'\ranzhi')
from base.util import BoxDriver,BasePage
from login_page import LoginPage

class AddUserPage(LoginPage):

    def add_user(self,account,realname,gender,dept,role,password1,password2,email):
        driver = self.driver
        # sleep(2)
        '''添加新成员'''
        # 点击后台管理
        # # 进入iframe
        driver.input('id account', account)
        driver.input('id realname', realname)
        if gender == '男':
            driver.click('id genderm')
        else:
            driver.click('id genderf')
        # 选择部门
        driver.select_by_value('id dept', dept)
        # 角色
        driver.select_by_value('id role', role)
        # 密码
        driver.input('id password1', password1)
        driver.input('id password2', password2)
        # 邮箱
        driver.input('id email', email)
        # 添加
        driver.click('id submit')
        sleep(2)
        # 跳转到最后一页
        total = driver.find_element('xpath /html/body/div/div/div/div[2]/div/div/div[2]/div/strong[2]').text.split(
            '/')
        driver.input('id _pageID', total)
        driver.click('id goto')
        sleep(1)
        # 断言
        accounts = driver.find_elements('xpath /html/body/div/div/div/div[2]/div/div/table/tbody/tr/td[3]')
        account = accounts[-1]  # 获取最后一个用户的用户名
        assert account.text == realname
        # 点击 添加成员

if __name__ == "__main__":
    # AddUser(BoxDriver()).add_user()
    pass
