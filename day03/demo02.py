'''登陆Ranzhi系统'''
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import random
from selenium.webdriver.support.ui import WebDriverWait


try: 
    driver = webdriver.Chrome()
    driver.get('http://localhost/ranzhi/www/sys/user-login.html')
    # 最大化
    driver.maximize_window()
    driver.implicitly_wait(8)

    '''登陆Ranzhi系统'''    
    # 用户名
    driver.find_element_by_id('account').send_keys('admin')
    # 密码
    driver.find_element_by_id('password').send_keys('123456')
    # 登陆
    driver.find_element_by_id('submit').click()


    '''添加新成员'''
    # 点击后台管理
    driver.find_element_by_id('s-menu-superadmin').click()

    # 进入iframe
    iframe = driver.find_element_by_id('iframe-superadmin')
    driver.switch_to.frame(iframe)
    
    # 点击添加成员
    driver.find_element_by_xpath('//*[@id="shortcutBox"]/div/div[1]/div/a').click()

    for i in range(41,45):
        username='user%d'%i
        driver.find_element_by_xpath('//*[@id="account"]').send_keys(username)

        driver.find_element_by_xpath('//*[@id="realname"]').send_keys(username)
    
        driver.find_element_by_xpath('//*[@id="genderm"]').click()
    
        #选择部门
        select=driver.find_element_by_id('dept')

        depts=Select(select)
    
        #按照index值选
        depts.select_by_index(random.randint(1,6))

        # # #按照index选——从0开始
        # # depts.select_by_index(1)
        # # #按照visible-test()选择
        # # depts.select_by_visible-text('/测试部')

        #角色
        select=driver.find_element_by_id('role')

        roles=Select(select)
    
        roles.select_by_index(random.randint(1,16))

        driver.find_element_by_xpath('//*[@id="password1"]').send_keys('123456')
        driver.find_element_by_xpath('//*[@id="password2"]').send_keys('123456')
        driver.find_element_by_xpath('//*[@id="email"]').send_keys('%s@163.com'%username)
        driver.find_element_by_xpath('//*[@id="submit"]').click()
        sleep(1)

        '''
        #跳转到最后一页
        total=driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/div[2]/div/strong[2]').text.split('/')
        driver.find_element_by_id('_pageID'.send_keys(total)
        driver.find_element_by_id('goto').click()
        '''
        
        #断言
        accounts=driver.find_elements_by_xpath('/html/body/div/div/div/div[2]/div/div/table/tbody/tr/td[3]')
        print(len(accounts))
        if len(accounts)==10:
            driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/div[2]/div/a[2]').click()
            sleep(1)
            accounts=driver.find_elements_by_xpath('/html/body/div/div/div/div[2]/div/div/table/tbody/tr/td[3]')
        sleep(1)
        account=accounts[-1]#获取最后一个用户的用户名
        assert account.text== username,'用户不存在'
        print('添加用户成功')
        sleep(1)
        driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div[2]/a[1]').click()
except Exception as e:
    print(e)
finally:
    sleep(2)
    driver.close()