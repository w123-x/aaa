'''鼠标操作'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
try:
    driver=webdriver.Chrome()
    driver.get('https://www.baidu.com')

    '''单击==click()'''
    # driver.find_element_by_id('kw').send_keys('登月')
    # btn=driver.find_element_by_id('su')
    # ActionChains(driver).click(btn).perform()
    # sleep(1)

    '''右击==context_click()'''
    # input=driver.find_element_by_id('kw')
    # ActionChains(driver).context_click(input).perform()#Actionchains:操作链，perform():同意开始执行
    
    '''双击==double_click()'''
    # driver.find_element_by_id('kw').send_keys('登月')
    # input=driver.find_element_by_id('kw')
    # ActionChains(driver).double_click(input).perform()

    '''悬停'''
    # news=driver.find_element_by_xpath('//*[contains(text(),"一箭双星")]')
    # ActionChains(driver).move_to_element(news).perform()
    # sleep(1)

    '''练习：关闭热榜'''
    set1=driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')
    # ActionChains(driver).move_to_element(set1).perform()
    sleep(1)
    Down=driver.find_element_by_xpath('//*[@id="s-user-setting-menu"]/a[1]')
    # ActionChains(driver).click(Down).perform()
    # sleep(1)
    ActionChains(driver).move_to_element(set1).click(Down).perform()
    sleep(2)
    '''拖拽'''
    
except Exception as e:
    print(e)
finally:
    sleep(2)
    driver.close()






