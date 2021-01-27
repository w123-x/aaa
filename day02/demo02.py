'''获取元素的属性的值'''

from selenium import webdriver
from time import sleep

try:
    driver=webdriver.Chrome()
    driver.get('https://www.baidu.com')

    #获取自定的属性
    href=driver.find_element_by_xpath('//*[@id="s-top-left"]/a[1]').get_attribute('href')#属性不是唯一的
    print(href)

    #获取元素的文本
    text=driver.find_element_by_xpath('//*[@id="s-top-left"]/a[1]').text#文本只有一个
    print(text)


except Exception as e:
    print(e)
finally:
    sleep(2)
    driver.close()


























