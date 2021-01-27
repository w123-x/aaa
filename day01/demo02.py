'''定位元素'''
from selenium import webdriver

'''使用id(唯一)定位'''
# #创建浏览器实例
# driver=webdriver.Chrome()
# #打开百度页面
# driver.get("https://www.baidu.com")#将结果封装起来了,直接放在driver里边了

# #定位输入框
# driver.find_element_by_id('kw').send_keys('成都疫情')#send_keys输入
# #点击“百度一下”
# driver.find_element_by_id('su').click()#click:点击

'''使用name(基本唯一)定位'''
# driver=webdriver.Chrome()
# driver.get('https://www.baidu.com')
# driver.find_element_by_name('wd').send_keys('嫦娥五号')
# driver.find_element_by_id('su').click()

'''使用class_name(一般是多个)定位'''
# #如果定位到多个元素,则默认返回第一个
# driver=webdriver.Chrome()
# driver.get('https://www.baidu.com')
# driver.find_element_by_class_name('s_ipt').send_keys('郑爽')
# driver.find_element_by_class_name('s_btn').click()

'''使用'''




























