from selenium import webdriver
from time import sleep
try:
    driver=webdriver.Chrome()
    driver.get('https://www.baidu.com')
    #窗口最大化
    driver.maximize_window()
    sleep(2)
    # #窗口最小化
    driver.minimize_window()
    #获取窗口的尺寸
    print(driver.get_window_size())

    driver.find_element_by_id('kw').send_keys('特朗普')
    sleep(2)
    #清空文本内容
    driver.find_element_by_id('kw').clear()
    sleep(1)
    driver.find_element_by_id('kw').send_keys('拜登')
    driver.find_element_by_id('su').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="1"]/h3/a').click()
    #切换到指定窗口,window_handles:获取当前窗口的域名
    driver.switch_to.window(driver.window_handles[1])
    sleep(3)
    driver.find_element_by_xpath('//*[@id="hotspotminingContent-578374"]/div[2]/div[1]/span[1]/a').click()
    sleep(2)


except Exception as e:
    print(e)
finally:
    sleep(2)
    driver.quit()