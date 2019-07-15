import doctest
#doctest模块可以提取注释中的代码执行
#doctest模块严格按照Python交互模式的输入提取
def mySum(x,y):
    '''
    get the sun from x and y
    :param x: firstNum
    :param y: SecondNum
    :return: sum
    #print前应该有一个空格
    example:
    >>> print(mySum(1,2))
    3

    '''
    return x + y

print(mySum(1,2))

#进行文档测试
doctest.testmod()