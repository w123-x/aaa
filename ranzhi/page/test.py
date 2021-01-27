import os,sys
#sys.path.append(x)#将x所在的目录加入到搜索目录中
sys.path.append(os.getcwd()+r'\ranzhi')
from login_page import LoginPage
from base.util import BoxDriver

class Wx:
    def aaa(self):
        self.a=LoginPage(BoxDriver(url='https://www.baidu.com'))
        self.a.login()
if __name__ == "__main__":
    Wx().aaa()