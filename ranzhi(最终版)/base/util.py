from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import random,yaml,time,openpyxl
import logging,sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

'''工具类'''

class BoxDriver:

    def __init__(self,browser_type='Chrome',url=None):
        # 根据传入的参数，创建响应的浏览器对象
        if browser_type == 'Chrome':
            self.driver = webdriver.Chrome()
        elif browser_type == 'Firefox':
            self.driver = webdriver.Firefox()
        elif browser_type == 'Opera':
            self.driver = webdriver.Opera()
        elif browser_type == 'Safari':
            self.driver = webdriver.Safari()
        elif browser_type == 'Ie':
            self.driver = webdriver.Ie()
        else:
            raise NameError('浏览器类型%s没找到！'%browser_type)

        self.driver.get(url)
        # 最大化
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)


    def get(self,url):
        '''
        打开指定的网页
        url: 网页地址
        '''
        self.driver.get(url)

    def maximize_window(self):
        '''
        窗口最大化
        '''
        self.driver.maximize_window()

    def minimize_window(self):
        '''
        窗口最小化
        '''
        self.driver.minimize_window()

    def implicitly_wait(self,second=10):
        '''
        隐式等待
        second:等待的最大时间，单位是秒
        '''
        self.driver.implicitly_wait(second)

    def wait(self,second):
        '''
        休眠
        second: 休眠时间，单位是秒
        '''
        time.sleep(second)

    def webdriver_wait(self,selector,timeout=5,frequency=0.5):
        '''
        显式等待
        selector: 自定义定位方式
        timeout: 超时时间 秒
        frequency: 采样间隔 秒
        '''
        locator = self.convert_selector_to_locator(selector)
        return WebDriverWait(self.driver,timeout,frequency).until(EC.presence_of_element_located(locator))
        

    def convert_selector_to_locator(self,selector,separator=' '):
        '''
        定位方式解析器，将形如：
        'id account' 
        的自定义方式，解析为selenium标准定位方式：
        By.ID,'account'
        selector: 自定义定位方式
        sepatrator: 分隔方式，默认使用' '来分隔
        '''
        # 定位方式
        by = selector.split(separator)[0].strip()
        # 定位方式对应的值
        value = selector.split(separator)[1].strip()

        if by == 'id' or by == 'i':
            locator = (By.ID,value)
        elif by == 'name' or by == 'n':
            locator = (By.NAME,value)
        elif by == 'class_name' or by == 'c':
            locator = (By.CLASS_NAME,value)
        elif by == 'tag_name' or by == 't':
            locator = (By.TAG_NAME,value)
        elif by == 'link_text' or by == 'l':
            locator = (By.LINK_TEXT,value)
        elif by == 'partial_link_text' or by == 'p':
            locator = (By.PARTIAL_LINK_TEXT,value)
        elif by == 'xpath' or by == 'x':
            locator = (By.XPATH,value)
        elif by == 'css_selector' or by == 'cs':
            locator = (By.CSS_SELECTOR,value)
        else:
            raise NameError('请输入一个合法的定位方式！')

        return locator

    def find_element(self,selector):
        '''
        定位单个元素
        selector: 自定义定位方式
        '''
        locator = self.convert_selector_to_locator(selector)
        return self.driver.find_element(*locator)

    def find_elements(self,selector):
        '''
        定位多个元素
        selector: 自定义定位方式
        '''
        locator = self.convert_selector_to_locator(selector)
        return self.driver.find_elements(*locator)

    def input(self,selector,text):
        '''
        向元素输入文本
        selector: 自定义定位方式
        text: 要输入的文本
        '''
        element = self.find_element(selector)
        element.clear() # 写文本之前，先清空一下
        element.send_keys(text)

    def click(self,selector):
        '''
        单击元素
        selector: 自定义定位方式
        '''
        self.find_element(selector).click()

    def switch_to_frame(self,selector):
        '''
        进入到指定的iframe元素
        selector: 自定义定位方式
        '''
        iframe = self.find_element(selector)
        self.driver.switch_to.frame(iframe)

    def select_by_index(self,selector,index):
        '''
        根据index选择下拉选择框的内容
        selector: 自定义选择器
        index: 下标
        '''
        select = self.find_element(selector)
        options = Select(select)
        options.select_by_index(index)

    def select_by_value(self,selector,value):
        '''
        根据value选择下拉选择框的内容
        selector: 自定义选择器
        value: value属性的值
        '''
        select = self.find_element(selector)
        options = Select(select)
        options.select_by_value(value)

    def select_by_visible_text(self,selector,visible_text):
        '''
        根据visible_text选择下拉选择框的内容
        selector: 自定义选择器
        visible_text: 可见文本
        '''
        select = self.find_element(selector)
        options = Select(select)
        options.select_by_visible_text(visible_text)

    def close(self):
        '''
        关闭当前浏览器窗口
        '''
        self.driver.close()

    def quit(self):
        '''
        退出浏览器
        '''
        self.driver.quit()

class BasePage:

    def __init__(self,driver:BoxDriver):
        self.driver = driver

class GetYaml:
    def get(self,path):
        '''
        读取Yaml格式文件，返回一个字典类型的数据
        path: yaml文件的路径
        '''
        with open(path,'r',encoding='utf-8') as file:
            config = yaml.load(file.read(),Loader=yaml.FullLoader)
            return config

class GetExcel:

    def get(self,path,worksheet):
        '''
        读取Excel格式文件，返回一个列表类型的数据
        path: excel文件的路径
        worksheet: 工作表的名称
        '''
        # 打开工作簿
        workbook = openpyxl.load_workbook(path)

        # 打开指定的工作表
        login_success = workbook[worksheet]

        # [('admin','123456'),('user0','123456')]
        return [tuple(cell.value for cell in row) for row in login_success][1:]

class GetCSV:

    def get(self,path):
        '''
        读取CSV格式文件，返回一个列表类型的数据
        path: CSV文件的路径
        '''
        with open(path,'r',encoding='utf-8') as file:
            lines = file.readlines()
            return [tuple(e.strip() for e in line.split(',')) for line in lines][1:]

class GetLogger:

    def __init__(self,path,level=logging.DEBUG):
        '''
        path: 日志文件路径
        '''
        # 设置日志文件路径
        self.path = path
        # 创建日志
        self.logger = logging.getLogger()
        # 设置日志级别
        self.logger.setLevel(level)
        # 设置日志输出的格式
        self.formatter = logging.Formatter('[%(asctime)s]-[%(filename)s]-[%(levelname)s]:%(message)s')

    def console(self,level,message):
        '''
        level: 日志等级
        message: 日志要输出的信息
        '''
        '''写入到文件中'''
        # 创建一个文件处理器
        fh = logging.FileHandler(self.path,encoding='utf-8')
        # 设置文件日志级别
        fh.setLevel(logging.DEBUG)
        # 设置日志的格式
        fh.setFormatter(self.formatter)
        # 将文件处理器添加到日志中
        self.logger.addHandler(fh)

        '''写入到控制台'''
        # 创建一个流处理器
        sh = logging.StreamHandler(sys.stdout) # standard output
        # 设置日志等级
        sh.setLevel(logging.DEBUG)
        # 设置日志格式
        sh.setFormatter(self.formatter)
        # 将流处理器添加到日志中
        self.logger.addHandler(sh)

        # 判断日志等级，进行相应的输出
        if level == 'debug':
            self.logger.debug(message)
        elif level == 'info':
            self.logger.info(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        elif level == 'critical':
            self.logger.critical(message)
        
        self.logger.removeHandler(sh)
        self.logger.removeHandler(fh)
        # 关闭文件处理器中打开的文件
        fh.close()

    def info(self,message):
        self.console('info',message)

    def debug(self,message):
        self.console('debug',message)

    def warning(self,message):
        self.console('warning',message)

    def error(self,message):
        self.console('error',message)

    def critical(self,message):
        self.console('critical',message)


class Email:

    def send(self,receivers,subject,content,path,smtpserver='smtp.163.com',port=25,sender='jingying0037@163.com',password='AVNCNFWSUJQEALFA'):
        '''
        receivers   收件人地址

        smtpserver  邮件服务器地址
        port        邮件服务器端口
        sender      发件人地址
        password    密码
        content     邮件正文
        path        附件地址
        '''

        # 创建邮件对象
        mail = MIMEMultipart()
        # 初始化发件人
        mail['from'] = sender
        # 添加收件人
        mail['to'] = receivers
        # 添加主题
        mail['subject'] = subject

        # 读取报告内容
        with open(path,'rb') as file:
            report = file.read()

        # 对附件进行编码
        attachment = MIMEText(report,'base64','utf-8')
        # 设置附件的类型
        attachment['Content-Type'] = 'application/octet-stream'
        # 设置附件的处理方式
        attachment['Content-Disposition'] = 'attchment;filename=%s'%path.split('/')[-1]
        # 添加附件
        mail.attach(attachment)

        
        # 对邮件正文进行编码
        body = MIMEText(content,'html','utf-8')
        # 添加正文
        mail.attach(body)

        # 创建SMTP对象
        smtp = smtplib.SMTP()
        # 连接服务器
        smtp.connect(smtpserver,port)
        # 登陆服务器
        smtp.login(sender,password)
        # 发送邮件
        smtp.sendmail(sender,receivers.split(';'),mail.as_string())
        # 关闭服务器
        smtp.close()
        print('邮件发送完毕！')


if __name__ == "__main__":
        receivers = 'jingying0037@163.com'
        subject = 'Ranzhi自动化测试报告'
        content = '''
        <p>Dear Mike,</p>
        <p>&nbsp;&nbsp;这是Ranzhi项目的测试报告，请查收!</p>
        <p>此致</p>
        <p>Tom</p>
        '''
        path = r'ranzhi/report/report_2020-12-16_10_06_59.html'
        Email().send(receivers,subject,content,path)