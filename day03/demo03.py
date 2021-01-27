'''登陆Ranzhi系统'''
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import random
from selenium.webdriver.support.ui import WebDriverWait
from util import BoxDriver #从模块里边导入类
class AddUser:
    def add_user(self,uname='admin',upwd='123456'):
        try: 
            #driver = webdriver.Chrome()
            driver=BoxDriver()
            driver.get('http://localhost/ranzhi/www/sys/user-login.html')
            # 最大化
            driver.maximize_window()
            driver.implicitly_wait(8)
            # '''登陆Ranzhi系统'''    
            driver.input('id account',uname)
            driver.click('id submit')








            # '''添加新成员'''
            # # 点击后台管理
            driver.click('id s-menu-superadmin')
            
            # # 进入iframe
            driver.switch('id iframe-superadmin')
            sleep(1)

            # 点击添加成员
            driver.click('xpath //*[@id="shortcutBox"]/div/div[1]/div/a')
            sleep(1)

            for i in range(45,48):
                username='user%d'%i
                driver.input('id account',username)

                driver.input('id realname',username)
            
                driver.click('id genderm' if i%2==0 else 'id genderf')
            
                #选择部门
                driver.select_by_index('id dept',random.randint(1,6))
            #     #角色
                driver.select_by_index('id role',random.randint(1,16))

                driver.input('xpath //*[@id="password1"]','123456')
                driver.input('xpath //*[@id="password2"]','123456')
                driver.input('xpath //*[@id="email"]','%s@163.com'%username)
                driver.click('xpath //*[@id="submit"]')
            #     sleep(1)

            #     '''
            #     #跳转到最后一页
                total = driver.find_element('xpath /html/body/div/div/div/div[2]/div/div/div[2]/div/strong[2]').text.split('/')
                driver.input('id _pageID', total)
                driver.click('id goto')
            #     '''
                
            #     # 断言
                accounts = driver.find_element1('xpath /html/body/div/div/div/div[2]/div/div/table/tbody/tr/td[3]')
                account = accounts[-1] # 获取最后一个用户的用户名
                assert account.text == username

            #     # 点击 添加成员
                driver.click('link_text 添加成员')
        except Exception as e:
            print(e)
        finally:
            sleep(2)
            #driver.close()
            
if __name__ == "__main__":
    AddUser().add_user()