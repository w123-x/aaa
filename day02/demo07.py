'''登陆Ranzhi系统'''
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

try:
    driver=webdriver.Chrome()
    driver.get('http://localhost/ranzhi/www/sys/user-login-L3JhbnpoaS93d3cvc3lzLw==.html')
    # #窗口最大化
    # driver.maximize_window()
    #隐式等待
    driver.implicitly_wait(10)
    '''登陆页面'''
    #用户名
    driver.find_element_by_xpath('//*[@id="account"]').send_keys('admin')
    # sleep(1)
    #密码
    driver.find_element_by_xpath('//*[@id="password"]').send_keys('123456')
    driver.find_element_by_clss
    # sleep(1)
    #登陆
    driver.find_element_by_xpath('//*[@id="submit"]').click()
    # sleep(2)
    '''添加成员'''
    driver.find_element_by_xpath('//*[@id="s-menu-4"]/button').click()
    # sleep(1)
    #进入iframe
    iframe=driver.find_element_by_id('iframe-4')
    driver.switch_to.frame(iframe)
    # sleep(1)
    #创建文档库
    driver.find_element_by_xpath('//*[@id="createButton"]').click()
    # sleep(1)
    #文档库类型
    select=driver.find_element_by_xpath('//*[@id="libType"]')
    Select(select).select_by_index(0)
    # sleep(1)
    #文档库名称
    driver.find_element_by_xpath('//*[@id="name"]').send_keys('python')
    # sleep(1)
    #授权用户
    driver.find_element_by_xpath('//*[@id="users_chosen"]/ul').click()
    driver.find_element_by_xpath('//*[@id="users_chosen"]/div/ul/li').click()
    # sleep(1)
    #授权分组
    driver.find_element_by_xpath('//*[@id="groupTR"]/td/label[1]').click()
    # sleep(1)
    driver.find_element_by_xpath('//*[@id="groupTR"]/td/label[2]').click()
    # sleep(1)
    driver.find_element_by_xpath('//*[@id="groupTR"]/td/label[3]').click()
    # sleep(1)
    driver.find_element_by_xpath('//*[@id="groupTR"]/td/label[4]').click()
    # sleep(1)
    driver.find_element_by_xpath('//*[@id="groupTR"]/td/label[5]').click()
    # sleep(1)
    #保存
    driver.find_element_by_xpath('//*[@id="submit"]').click()
    


except Exception as e:
    print(e)

finally:
    sleep(2)
    driver.close()





















    