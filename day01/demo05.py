'''xpath定位'''
from selenium import webdriver
from time import sleep
try:
    driver=webdriver.Chrome()
    driver.get('https://www.baidu.com')
    #相对定位
    driver.find_element_by_xpath('//*[@id="kw"]').send_keys('郑爽')
    #绝对定位
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[5]/div/div/form/span[2]/input').click()
except Exception as e:
    print(e)
finally:
    sleep(2)
    driver.close()











