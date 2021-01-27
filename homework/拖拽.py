from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains



'''拖拽'''
news=driver.find_element_by_xpath('//*[contains(text()."新增确诊")]')
input=driver.find_element_by_id('kw')
ActionChains(driver).drag_and_drop(news,input).move_to_element(input).release(input).perform()











