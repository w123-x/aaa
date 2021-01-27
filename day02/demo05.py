'''滚动条'''

from selenium import webdriver
from time import sleep
try:

    driver=webdriver.Chrome()
    driver.get('https://www.baidu.com')
    
    #设置窗口尺寸
    driver.set_window_size(1000,300)
    sleep(2)
    
    #获取目标元素
    target=driver.find_element_by_xpath('//*[contains(text(),"百度热榜")]')
    
    #滚动到目标元素,直接运行javascript代码(script中将传入的参数自动封装成列表)

    driver.execute_script('arguments[0].scrollIntoView();',target)#arguments[0]:取第一个参数；scrollIntoView():滚动文档窗口






except Exception as e:
    print(e)
finally:
    sleep(2)
    driver.close()






