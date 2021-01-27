'''css定位'''
from selenium import webdriver
from time import sleep
try:
    driver=webdriver.Chrome()
    driver.get('https://www.baidu.com')
    #css:层叠样式表，#:代表id
    driver.find_element_by_css_selector('#kw').send_keys('月壤')
    driver.find_element_by_css_selector('#su').click()
except Exception as e:
    print(e)
finally:
    sleep(2)
    driver.quit()














