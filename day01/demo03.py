from selenium import webdriver
import time

'''使用tag_name定位'''
driver=webdriver.Chrome()
driver.get(r'D:\workspace\selenium\day01\demo.html')

#用户
driver.find_element_by_tag_name('input').send_keys('月壤')

#获取多个元素(用find_elements_by_tag_name,并且返回的是列表,如果只有一个元素,返回的也是列表)
inputs=driver.find_elements_by_tag_name('input')
print(inputs)
#返回
# [<selenium.webdriver.remote.webelement.WebElement (session="8ce9c36b148f66b4258d617e4165aa47", element="7f2942ed-fa7d-4c6c-b40d-e3e17100c5e6")>, 
# <selenium.webdriver.remote.webelement.WebElement (session="8ce9c36b148f66b4258d617e4165aa47", element="22db6e48-175e-49ea-94e2-7181a8da94b7")>, 
# <selenium.webdriver.remote.webelement.WebElement (session="8ce9c36b148f66b4258d617e4165aa47", element="9a8054d1-1bf7-4cdb-83ca-205384aead79")>]
#密码
inputs[1].send_keys('123456')
time.sleep(2)
#登录
inputs[2].click()

#关闭浏览器
driver.close()

































































