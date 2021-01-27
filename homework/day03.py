'''登陆Ranzhi系统'''
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait

driver=webdriver.Chrome()
driver.get('http://localhost/ranzhi/www/sys/user-login-L3JhbnpoaS93d3cvc3lzLw==.html')
driver.implicitly_wait(8)
# #窗口最大化
# driver.maximize_window()
'''登陆页面'''
#用户名
driver.find_element_by_xpath('//*[@id="account"]').send_keys('admin')

#密码
driver.find_element_by_xpath('//*[@id="password"]').send_keys('123456')

#登陆
driver.find_element_by_xpath('//*[@id="submit"]').click()


driver.find_element_by_xpath('//*[@id="s-menu-superadmin"]/button').click()
#进入iframe
iframe=driver.find_element_by_id('iframe-superadmin')
driver.switch_to.frame(iframe)
# #点击添加成员    
driver.find_element_by_xpath('//*[@id="shortcutBox"]/div/div[1]/div/a').click()
user4=['citi','Citi','13','top','citi@163.com']
user3=['citc','Citc','13','top','citc@163.com']
user2=['citb','Citb','13','top','citb@163.com']
list2=[user3,user2]
for list1 in list2:
    driver.find_element_by_xpath('//*[@id="account"]').send_keys(list1[0])
    
    driver.find_element_by_xpath('//*[@id="realname"]').send_keys(list1[1])
   
    driver.find_element_by_xpath('//*[@id="genderm"]').click()
   
    #选择部门
    select=driver.find_element_by_id('dept')

    depts=Select(select)
   
    #按照value值选
    depts.select_by_value(list1[2])
    
    # # #按照index选——从0开始
    # # depts.select_by_index(1)
    # # #按照visible-test()选择
    # # depts.select_by_visible-text('/测试部')

    #角色
    select=driver.find_element_by_id('role')
    
    roles=Select(select)
   
    roles.select_by_value(list1[3])
    
    driver.find_element_by_xpath('//*[@id="password1"]').send_keys('123456')
    driver.find_element_by_xpath('//*[@id="password2"]').send_keys('123456')
    driver.find_element_by_xpath('//*[@id="email"]').send_keys(list1[4])
    driver.find_element_by_xpath('//*[@id="submit"]').click()
    driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div[2]/a[1]').click()




   


