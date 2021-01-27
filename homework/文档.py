'''登陆Ranzhi系统'''
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from util import BoxDriver
class AddWord:
    def add_word(self,uname='admin',upwd='123456'):
        try:
           driver=BoxDriver()
           driver.get('http://localhost/ranzhi/www/sys/user-login-L3JhbnpoaS93d3cvc3lzLw==.html')
           driver.implicitly_wait(8)
           driver.input('id account',uname)
           driver.input('id password',upwd)
           driver.click('id submit')
           driver.click('xpath //*[@id="s-menu-4"]/button')
           #进入iframe
           driver.switch('id iframe-4')
           driver.maximize_window()
           #进入python库
           driver.click('xpath //*[@id="libs"]/div/div/div/a')
           for i in range(22,25):
                #创建文档//*[@id="menuActions"]/a //*[@id="menuActions"]/a
                driver.click('xpath //*[@id="menuActions"]/a')
                #授权用户
                driver.click('xpath //*[@id="users_chosen"]/ul')
                driver.click('xpath //*[@id="users_chosen"]/div/ul/li')
                #文档类型
                driver.click('xpath //*[@id="typetext"]')
                #文档标题
                wordname='python用法'+str(i)
                driver.input('xpath //*[@id="title"]',wordname)
                #进入iframe
                driver.switch('id ueditor_0')
                #写文档正文
                driver.input('xpath /html/body/p','你好%d！'%i)
                #回到frame父级
                driver.driver.switch_to.parent_frame()#转回到frame的父级
                #关键字
                driver.input('id keywords','python语句%d'%i)
                #摘要
                driver.input('xpath //*[@id="digest"]','py语句%d'%i)
                #附件
                driver.input('xpath //*[@id="fileBox1"]/tbody/tr/td[1]/div/input','D:\workspace\selenium\自动化测试.txt')
                driver.input('xpath //*[@id="fileBox1"]/tbody/tr/td[2]/input','python文档%d'%i)
                #附件
                driver.input('xpath //*[@id="fileBox2"]/tbody/tr/td[1]/div/input','D:\workspace\selenium\自动化测试.txt')
                driver.input('xpath //*[@id="fileBox2"]/tbody/tr/td[2]/input','python_文档%d'%i)
                sleep(1)
                 #保存
                driver.click('id submit')
                sleep(2)
                # 断言
                accounts = driver.find_element1('xpath //*[@id="docList"]/tbody/tr/td[2]')
                if len(accounts)>20:
                    driver.click('xpath /html/body/div/div[3]/div[2]/div/div[2]/div/a[2]')
                    accounts = driver.find_element1('xpath //*[@id="docList"]/tbody/tr/td[2]')
                account = accounts[0] # 获取最后一个用户的用户名
                assert account.text == wordname,'文件标题不符'
                print(wordname+'添加成功')
        except Exception as e:
            print(e)
        finally:
            sleep(2)
            driver.driver.close()
if __name__ == "__main__":
    AddWord().add_word()