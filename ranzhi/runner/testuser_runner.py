import os,sys
#sys.path.append(x)#将x所在的目录加入到搜索目录中
sys.path.append(os.getcwd()+r'\ranzhi')#写绝对路径
from base.HTMLTestRunner import HTMLTestRunner
import unittest,time

class TestRunner1:

    def runner(self):
        '''挑选用例'''
        #创建测试套件
        suite=unittest.TestSuite()#testsuite:一套用例
        #添加测试用例
        suite.addTests(unittest.TestLoader().discover('./ranzhi/test',pattern='adduser_test2.py'))#discover:发现;pattern:格式
        #生成一个时间戳stamp:戳
        # time.strftime:系统当前时间
        timestamp = time.strftime('%Y-%m-%d_%H_%M_%S')#f—->formatting:格式
        #创建html报告文件,html不存在追加，是独立的文件
        report=open('./ranzhi/report/report_%s.html'%timestamp,'wb')
        #创建用例运行器，用于运行用例并生成报告
        test_runner=HTMLTestRunner(stream=report,title='Ranzhi自动话测试报告',description='报告的详细描述')
        #运行
        test_runner.run(suite)

if __name__ == "__main__":
    TestRunner1().runner()
    # print(os.getcwd())#current working directory

















