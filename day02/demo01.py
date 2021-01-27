'''前进和后退'''

from selenium import webdriver
from time import sleep

try:
    driver=webdriver.Chrome()
    driver.get('https://www.baidu.com')
    driver.find_element_by_id('kw').send_keys('登月')
    driver.find_element_by_id('su').click()
    sleep(2)
    #后退back
    driver.back()
    sleep(2)
    #前进forward
    driver.forward()
    sleep(2)
    #刷新refresh
    driver.refresh()

except Exception as e:
    print(e)
finally:
    sleep(2)
    driver.close()











