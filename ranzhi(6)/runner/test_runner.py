from base.HTMLTestRunner import HTMLTestRunner
import unittest,time

class TestRunner:

    def runner(self):
        '''挑选用例'''
        # 创建测试套件
        suite = unittest.TestSuite()
        # 添加测试用例
        suite.addTests(unittest.TestLoader().discover('./ranzhi/test',pattern='login_test.py'))
        # 生成一个时间戳
        timestamp = time.strftime('%Y-%m-%d_%H_%M_%S')
        # 创建html报告文件
        report = open('./ranzhi/report/report_%s.html'%timestamp,'wb')
        # 创建用例运行器，用于运行用例斌生成报告
        test_runner = HTMLTestRunner(stream=report,title='Ranzhi自动化测试报告',description='报告的详细描述.....')
        # 运行
        test_runner.run(suite)

if __name__ == "__main__":
    TestRunner().runner()

