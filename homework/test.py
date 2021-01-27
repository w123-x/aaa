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
           #进入iframe//*[@id="block6"]/div[1]
        #    driver.switch('id iframe-3')//*[@id="block8"]/div[1]/div/a  //*[@id="block8"]/div[1]/div/button
        #    x=driver.driver.find_element_by_xpath('//*[@id="block6"]/div[1]')
           driver.switch('id iframe-3')
           sleep(1)
           x=driver.driver.find_element_by_xpath('//*[@id="block6"]/div[1]')
           print(x.text.split('\n'))
        except Exception as e:
            print(e)
        finally:
            sleep(2)
            driver.driver.close()
if __name__ == "__main__":
    Item().item()
    







































