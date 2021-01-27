'''link_text(链接文本,此文本指的是该超链接的全部文本)和partial_link_text(部分链接文本)'''

from selenium import webdriver
from time import sleep
try:
    driver=webdriver.Chrome()
    driver.get('https://www.baidu.com')

    #点击‘新闻’
    driver.find_element_by_link_text('新闻').click()

    #点击‘百度热榜’
    driver.find_element_by_partial_link_text('拜登').click()

except Exception as e:
    print(e)
finally:
    sleep(2)
    #退出浏览器
    driver.quit()
    #关闭当前窗口
    #driver.close()







































