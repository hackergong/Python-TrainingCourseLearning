'''
设计类
类名：见名知意，首字母大写，其他遵循驼峰原则
属性：见名知意，其他准许驼峰原则
行为(方法/功能)：见名知意，遵循驼峰原则
'''
'''
创建类
类：一种数据类型，本身并不占内存空间，和所学的number，string，
boolean等类似，用类创建实例化对象(变量)，对象占内存空间

格式：
class 类名(父类列表)：
    pass
    属性
    行为


'''

#object:基类，超类，所有类的父类，一般没有合适的父类就写object
class Person(object):
    #定义属性
    name = ""
    age = 9
    height = 0
    wight = 0
    #定义方法(定义函数)
    #注意：方法的参数必须以self当第一个参数
    #self代表类的实例(某个对象)
    def run(self):
        print("run")
    def eat(self,food):
        print("eat"+food)





















