'''入口程序'''
import os,sys
#sys.path.append(x)#将x所在的目录加入到搜索目录中
sys.path.append(os.getcwd()+r'\ranzhi')
from runner.testuser_runner import TestRunner1 
class Main:
    def start(self):
        TestRunner1().runner()
if __name__ == "__main__":
    # '''自动化代码入口'''
    Main().start()
























    