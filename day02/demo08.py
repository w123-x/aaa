'''等待'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

try:
    driver=webdriver.Chrome()
    driver.get('http://localhost/ranzhi/www/sys/user-login.html')

    '''sleep():休眠，特点:简单,缺点:不精确，浪费时间'''
    '''隐式等待：wait()'''
    driver.implicitly_wait(10)#标配#implicitly:页面加载完成,最多等10秒

    '''By.ID:指定定位的方式'''
    driver.find_element(By.ID,'account').send_keys('admin')

    '''显示等待:被等参数出来就可以了'''
    element=WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID,'password')))#参数必须是元组
    element.send_keys('123456')
    driver.find_element_by_id('submit').click()

except Exception as e:
    print(e)
finally:
    sleep(1)
    driver.close()





















































































