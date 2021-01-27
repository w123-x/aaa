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
    '''登陆页面'''
    #用户名
    driver.find_element_by_xpath('//*[@id="account"]').send_keys('admin')
    sleep(1)
    #密码
    driver.find_element_by_xpath('//*[@id="password"]').send_keys('123456')
    sleep(1)
    #登陆
    driver.find_element_by_xpath('//*[@id="submit"]').click()
    sleep(2)
    '''添加成员'''
    driver.find_element_by_xpath('//*[@id="s-menu-superadmin"]/button').click()
    sleep(1)
    #进入iframe
    iframe=driver.find_element_by_id('iframe-superadmin')
    driver.switch_to.frame(iframe)
    # #点击添加成员    
    # driver.find_element_by_xpath('//*[@id="shortcutBox"]/div/div[1]/div/a').click()
    # sleep(1)
    # user=driver.find_element_by_xpath('//*[@id="account"]').send_keys('tom')
    # sleep(1)
    # driver.find_element_by_xpath('//*[@id="realname"]').send_keys('Tom')
    # sleep(1)
    # driver.find_element_by_xpath('//*[@id="genderm"]').click()
    # sleep(1)
    # #选择部门
    # select=driver.find_element_by_id('dept')
    # sleep(1)
    # depts=Select(select)
    # sleep(1)
    # #按照value值选
    # depts.select_by_value('9')
    # sleep(1)
    # # #按照index选——从0开始
    # # depts.select_by_index(1)
    # # #按照visible-test()选择
    # # depts.select_by_visible-text('/测试部')

    # #角色
    # select=driver.find_element_by_id('role')
    # sleep(1)
    # roles=Select(select)
    # sleep(1)
    # roles.select_by_value('pm')
    # sleep(1)

    # # driver.find_element_by_xpath('//*[@id="dept"]').click()
    # # sleep(1)
    # # driver.find_element_by_xpath('//*[@id="dept"]/option[2]').click()
    # # sleep(1)
    # # driver.find_element_by_xpath('//*[@id="role"]').click()
    # # sleep(1)
    # # driver.find_element_by_xpath('//*[@id="role"]/option[2]').click()

    # sleep(1)
    # driver.find_element_by_xpath('//*[@id="password1"]').send_keys('123456')
    # sleep(1)
    # driver.find_element_by_xpath('//*[@id="password2"]').send_keys('123456')
    # sleep(1)
    # driver.find_element_by_xpath('//*[@id="email"]').send_keys('tom@163.com')
    # sleep(1)
    # driver.find_element_by_xpath('//*[@id="submit"]').click()

    #点击组织
    driver.find_element_by_xpath('//*[@id="mainNavbar"]/ul/li[2]/a').click()
    sleep(2)
    #删除成员
    drop=driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/table/tbody/tr[2]/td[11]/a[3]')
    sleep(1)
    ActionChains(driver).move_to_element(drop).perform()
    sleep(1)
    drop.click()
    sleep(2)
    #取消
    driver.switch_to.alert.dismiss()
    #删除成员
    drop=driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/table/tbody/tr[2]/td[11]/a[3]')
    sleep(1)
    ActionChains(driver).move_to_element(drop).perform()
    sleep(1)
    drop.click()
    sleep(2)
    #确定
    driver.switch_to.alert.accept()
    sleep(2)

    '''创建文档'''





























except Exception as e:
    print(e)
finally:
    sleep(2)
    driver.close()






