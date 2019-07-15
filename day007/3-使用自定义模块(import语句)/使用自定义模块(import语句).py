#引入模块
#import 语句
#格式：import module1[,module2[,module3[.....,modulen]]
#import time,random,os

#引入了自动以魔铠，不用加.py后缀
import tracy
#注意：一个模块只会被引入一次，不管你执行了多少次import。防止模块被多次引入

#使用模块中的内容
#格式：模块名:函数名/变量名
tracy.sayGood()