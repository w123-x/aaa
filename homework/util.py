from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
import random
from selenium.webdriver.common.by import By

'''工具类'''
#构造方法里边不允许有返回值
class BoxDriver:

    def __init__(self,browser_type='Chrome'):
        #根据传入的参数，创建相应的浏览器对象
        if browser_type == 'Chrome':
            self.driver=webdriver.Chrome()#创建谷歌浏览器
        elif browser_type == 'Firefox':
            self.driver=webdriver.Firefox()
        elif browser_type == 'Opera':
            self.driver=webdriver.Opera()
        elif browser_type == 'Safari':
            self.driver=webdriver.Safari()
        elif browser_type == 'Ie':
            self.driver=webdriver.Ie()
        else:
            raise NameError('浏览器类型%s未找到！'%browser_type)

    
    def get(self,url):

        '''
        打开指定的网页
        url:网页地址
        '''
        self.driver.get(url)
    def maximize_window(self):
        '''
        窗口最大化
        '''
        self.driver.maximize_window()
    def implicitly_wait(self,second=10):
        '''
        设置隐式等待
        second:最大等待秒数，默认参数是10
        '''
        self.driver.implicitly_wait(second)
    def convert_selector_to_locator(self,selector,separator=' '):
        '''
        定位方式解析器，将形如
        'id account'的自定义方式，解析为selenium标准定位方式：
        By.ID,'account'
        selector：自定义定位方式
        separator:分隔方式，默认使用' '来分隔
        '''
        #定位方式
        by=selector.split(separator)[0].strip()#strip():去掉字符串前后多余的空格或其他东西
        #定位方式对应的值
        value=selector.split(separator)[1].strip()

        if by=='id' or by=='i':
            locator=(By.ID,value)#locator:定位器
        elif by=='name' or by=='n':
            locator=(By.NAME,value)
        elif by=='class_name' or by=='c':
            locator=(By.CLASS_NAME,value)
        elif by=='tag_name' or by=='t':
            locator=(By.TAG_NAME,value)
        elif by=='link_text' or by=='l':
            locator=(By.LINK_TEXT,value)
        elif by=='partial_link_text' or by=='p':
            locator=(By.PARTIAL_LINK_TEXT,value)
        elif by=='xpath' or by=='x':
            locator=(By.XPATH,value)
        elif by=='css_selector' or by=='cs':
            locator=(By.CSS_SELECTOR,value)
        else:
            raise NameError('请输入一个合法的定位方式')
        return locator

    def find_element(self,selector):#*变量名写在形参里边是封装为元组
        '''
        selector:定位方式
        '''
        # by,value=self.convert_selector_to_locator(seletor)
        # self.driver.find_element(by.value)
        locator=self.convert_selector_to_locator(selector)
        return self.driver.find_element(*locator)#*变量名写在实参里边是拆包为元素
    def find_element1(self,selector):#*变量名写在形参里边是封包为元组
        '''
        selector:定位方式
        '''
        # by,value=self.convert_selector_to_locator(seletor)
        # self.driver.find_element(by.value)
        locator=self.convert_selector_to_locator(selector)
        return self.driver.find_elements(*locator)
    def input(self,selector,text):
        '''
        向元素输入文本
        selector:自定义定位方式
        text:要输入的文本
        '''
        element=self.find_element(selector)
        element.send_keys(text)
    def click(self,selector):
        '''
        单击元素
        selector:自定义定位方式
        '''
        self.find_element(selector).click()

    def switch(self,selector):
        '''
        进入到指定的iframe元素
        selector：自定义定位方式
        '''
        iframe=self.find_element(selector)
        self.driver.switch_to.frame(iframe)

    def select_by_index(self,selector,index):
        '''
        根据index选择下拉选择框的内容
        selector:自定义选择器
        value:value属性的值
        '''
        select=self.find_element(selector)
        options=Select(select)
        options.select_by_index(index)

    def select_by_value(self,selector,value):
        '''
        根据index选择下拉选择框的内容
        selector:自定义选择器
        index:下标
        '''
        select=self.find_element(selector)
        options=Select(select)
        options.select_by_value(value)
    def select_by_visible_text(self,selector,visible_text):
        '''
        根据index选择下拉选择框的内容
        selector:自定义选择器
        visible_text:可见文本
        '''
        select=self.find_element(selector)
        options=Select(select)
        options.select_by_index(visible_text)

if __name__ == "__main__":
    BoxDriver()



















