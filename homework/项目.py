from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from util import BoxDriver
import random

class Item:
    def item(self,uname='admin',upwd='123456'):
        try:
           driver=BoxDriver()
           driver.get('http://localhost/ranzhi/www/sys/user-login-L3JhbnpoaS93d3cvc3lzLw==.html')
           driver.implicitly_wait(8)
           driver.input('id account',uname)
           driver.input('id password',upwd)
           driver.click('id submit')
           #点击项目
           driver.click('xpath //*[@id="s-menu-3"]/button/img')
           #进入iframe
           driver.switch('id iframe-3')
           for i in range(5,10):
                #点击添加区块//*[@id="dashboard"]/div[2]/a
                driver.click('xpath //*[@id="dashboard"]/div[2]/a')
                sleep(1)
                #点击区块
                #driver.click('id blocks')
                sleep(1)
                #选择“任务列表”//*[@id="blocks"]
                driver.select_by_index('id blocks',1)
                #区块名称
                driver.input('id title','item%d'%i)
                #外观
                driver.click('id grid')
                #选择外观宽度//*[@id="grid"]
                driver.select_by_index('xpath //*[@id="grid"]',i%5)
                #选择外观颜色
                driver.click('xpath //*[@id="ajaxForm"]/table/tbody/tr[2]/td/div/div/div/button')
                sleep(3)
                ran7=random.randint(1,7)
                driver.click('xpath //*[@id="ajaxForm"]/table/tbody/tr[2]/td/div/div/div/div/li[%d]/button'%ran7)
                sleep(1)
                #点击类型//*[@id="paramstype_chosen"]/div/ul/li[2] //*[@id="paramstype_chosen"]/div/ul/li[1] //*[@id="paramstype_chosen"]/div/ul/li[3]
                driver.click('xpath //*[@id="paramstype_chosen"]/a')
                sleep(1)
                ran6=random.randint(1,6)
                driver.click('xpath //*[@id="paramstype_chosen"]/div/ul/li[%d]'%ran6)
                #数量
                driver.input('id params[num]',15)
                #排序
                driver.click('xpath //*[@id="paramsorderBy_chosen"]/a')
                sleep(1)
                #选择排序
                driver.click('xpath //*[@id="paramsorderBy_chosen"]/div/ul/li[%d]'%ran7)
                #任务状态
                driver.click('xpath //*[@id="paramsstatus_chosen"]/ul')
                sleep(1)
                driver.click('xpath //*[@id="paramsstatus_chosen"]/div/ul/li[%d]'%ran7)
                sleep(2)
                #保存
                driver.click('id submit')

                sleep(4)
        except Exception as e:
            print(e)
        finally:
            sleep(2)
            driver.driver.close()
if __name__ == "__main__":
    Item().item()
    







































