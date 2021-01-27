'''入口程序'''
from runner.test_runner import TestRunner

class Main:

    def start(self):
        TestRunner().runner()

if __name__ == "__main__":
    '''自动化代码入口'''
    Main().start()