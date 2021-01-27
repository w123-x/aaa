import unittest

'''单元测试'''

# 要使用单元测试，必须继承TestCase类
class Test01(unittest.TestCase):
    
    # 该方法在所有用例前执行，并且只执行一次
    @classmethod
    def setUpClass(self):
        print('在所有用例前执行！')

    # 该方法在所有用例后执行，并且只执行一次
    @classmethod
    def tearDownClass(self):
        print('在所有用例之后执行！')

    # 重新父类的setUp方法
    # 该方法会在每一个测试用例前执行
    def setUp(self):
        print('开始执行用例！')

    # 该方法会在每一个测试用例后执行
    def tearDown(self):
        print('用例执行结束！')

    # 测试用例方法名必须以testxxx开头
    # 用例按照方法名的ASCII码顺序来执行
    def test01(self):
        print('执行测试用例test01......')

    def test02(self):
        print('执行测试用例test02......')

    def testabc(self):
        print('执行测试用例testabc......')

if __name__ == "__main__":
    # Test01().test01()
    # Test01().test02()
    unittest.main()