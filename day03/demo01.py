from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
try:
    driver=webdriver.Chrome()
    driver.get('http://localhost/ranzhi/www/sys/user-login-L3JhbnpoaS93d3cvc3lzLw==.html')
    driver.implicitly_wait(8)
    driver.maximize_window()
    driver.find_element_by_xpath('//*[@id="account"]').send_keys('hmf')
    driver.find_element_by_xpath('//*[@id="password"]').send_keys('123456')
    driver.find_element_by_xpath('//*[@id="submit"]').click()
    #获取用户真实姓名
    realname=driver.find_element_by_xpath('//*[@id="mainNavbar"]/div/ul[1]/li/a').text
    print(realname)
    #判断
    # if realname=='Hmf':
    #     print('登陆成功')
    # else:
    #     print('登录失败')
    #如果断言失败，则抛出异常
    assert realname=='Hmf','登陆失败！'#断言,assert:断言；
    #断言realname=='Tom Cruse',否则登陆失败
    #断言不影响程序的执行

    #获取登陆成功以后的url
    current_url=driver.current_url
    print('url==%s'%current_url)   
    assert current_url== 'http://localhost/ranzhi/www/sys/index.html','登录失败'
    
    #获取当前页面的title
    current_title=driver.title
    print('title==%s'%current_title)
    assert current_title=='然之协同','登录失败'
    print('用例执行结束！')
except Exception as e:
    print(e)
finally:
    driver.close()
