import unittest
from unittestexample import mySum
from unittestexample import mySub


class Test(unittest.TestCase):
    def setUp(self):
        print("开始测试时，自动调用")
    def tearDown(self):
        print("测试结束时,自动调用")

    #为了测试mySum
    def test_mySum(self):
        self.assertEqual(mySum(1,2),3,"加法有误")

    def test_mySub(self):
        self.assertEqual(mySub(2,1),1,"减法有误")

if __name__ =="__main__":
    unittest.main()
