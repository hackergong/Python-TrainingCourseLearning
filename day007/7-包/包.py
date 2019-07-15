'''

思考：如果不同的人编写的模块同名怎么办？

解决：为了解决模块命名的冲突引入按目录来组织模块的方法
称为包。

特点：引入了包以后，只要顶层的包不与其他人发生冲突，那么
模块都不会与别人发送冲突

注意：目录只有包含一个叫做“__init__.py”的文件才被认作是一个包，
主要为了避免一些滥竽充数的名字。基本上这个文件中什么也不用写。
比如a,b
#当没有__init__.py也能执行，但是之后会写一些内容
'''
#
import a.tracy
import b.tracy
import a.kaige

a.tracy.sayGood()
b.tracy.sayGood()
a.kaige.sayGood()











