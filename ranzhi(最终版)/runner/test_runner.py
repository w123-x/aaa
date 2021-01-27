import os,sys
sys.path.append(os.getcwd()+r'\ranzhi')

from base.HTMLTestRunner import HTMLTestRunner
import unittest,time
from base.util import Email

class TestRunner:

    def runner(self):
        '''挑选用例'''
        # 创建测试套件
        suite = unittest.TestSuite()
        # 添加测试用例
        suite.addTests(unittest.TestLoader().discover('./ranzhi/test',pattern='login_test.py'))
        # 生成一个时间戳
        timestamp = time.strftime('%Y-%m-%d_%H_%M_%S')
        # 创建报告路径
        path = './ranzhi/report/report_%s.html'%timestamp
        # 创建html报告文件
        report = open(path,'wb')
        # 创建用例运行器，用于运行用例斌生成报告
        test_runner = HTMLTestRunner(stream=report,title='Ranzhi自动化测试报告',description='报告的详细描述.....')
        # 运行
        test_runner.run(suite)
        # 发送报告
        receivers = 'jingying0037@163.com;test_893150990@163.com;hmf4611@163.com;18215367528@163.com;sunwei2159@163.com'
        subject = 'Ranzhi自动化测试报告'
        content = '''
        <p>Dear Mike,</p>
        <p>&nbsp;&nbsp;这是Ranzhi项目的测试报告，请查收!</p>
        <p>此致</p>
        <p>Tom</p>
        '''
        Email().send(receivers,subject,content,path)

if __name__ == "__main__":
    TestRunner().runner()

