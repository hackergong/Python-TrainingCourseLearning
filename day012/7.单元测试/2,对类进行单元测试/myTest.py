import unittest
from person import Person

class Test(unittest.TestCase):
    #需要有初始化就需要写

    def test_init(self):
        p = Person("hanhan",20)
        self.assertEqual(p.name,"hanhan","属性赋值错误")

    def test_getAge(self):
        p = Person("hanhan",22)
        self.assertEqual(p.getAge(),p.age,"getAge函数有误")

if __name__ == "__init__":
    unittest.main()