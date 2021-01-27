from selenium import webdriver
from time import sleep

try:
    driver=webdriver.Chrome()
    driver.get('https://www.baidu.com')
    #单机刷新按钮

    #根据属性定位
    # driver.find_element_by_xpath('//*[@class="hot-refresh-text"]').click()
    
    #根据文本精确定位
    # driver.find_element_by_xpath('//*[text()="换一换"]').click()

    #根据文本模糊定位
    # driver.find_element_by_xpath('//*[contains(text(),"三胎")]').click()#contains:包含,text():全部文本
    #根据属性模糊定位
    # driver.find_element_by_xpath('//*[contains(@class,"title-text")]').click()

except Exception as e:
    print(e)
finally:
    sleep(2)
    driver.quit()









