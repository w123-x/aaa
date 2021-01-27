'''键盘与鼠标操作'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

try:
    driver=webdriver.Chrome()
    driver.get('https://www.baidu.com')

    input=driver.find_element_by_id('kw')
    input.send_keys('拜登')
    #选中7
    input.send_keys(Keys.CONTROL,'A')
    sleep(2)
    #复制
    input.send_keys(Keys.CONTROL,'C')
    sleep(2)
    #粘贴
    input.send_keys(Keys.CONTROL,'V')
    input.send_keys(Keys.CONTROL,'V')
    input.send_keys(Keys.CONTROL,'V')
    sleep(2)
    #回车
    input.send_keys(Keys.ENTER)
    sleep(1)





except Exception as e:
    print(e)
finally:
    sleep(2)
    driver.close()