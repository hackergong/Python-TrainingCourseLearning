'''
'''
'''
UTC(世界协调时间）：格林尼治时间，世界标准时间，在中国来说是UTC+8
DST（夏令时）：是一种节约能源而认为规定时间制度，在夏季调快1个小时

时间的表示形式：
1.时间戳
以整型或浮点型表示时间的一个以秒为单位的时间间隔，这个时间间隔的基础值是从1970年1月1日零点开始算起

2.元组
一种Python的数据结构表示，这个元组有9个整型内容year,month,day015,hours,minutes,seconds,weekday,Julia day015,flag(1或-1或0)

3.格式化的字符串
%a  本地（locale）简化星期名称
%A  本地完整星期名称
%b  本地简化月份名称
%B  本地完整月份名称
%c  本地相应的日期和时间表示
%d  一个月中的第几天（01-31）
%H  一天中的第几个小时（24小时制，00-23）
%I  第几个小时（12小时制，01-12）
%j  一年中的第几天（001-366）
%m  月份（01-12）
%M  分钟数（00-59）
%p  本地am或者pm的相应符
%s  秒（01-61）
%U  一年中的星期数。（00-53星期天是一个星期的开始。）第一个星期天之前的所有天数都放在第0周
%w  一个星期中的第几天（0-6,0是星期天）
%W  和%U基本相同，不同的是%W以星期一为一个星期的开始
%x  本地相应日期
%X  本地相应时间
%y  去掉世纪的年份（00-99）
%Y  完整的年份
%Z  时区的名字（如果不存在空字符）
%%  '%'字符

2017-07-28 14:49:45

'''
import time


#返回当前时间的时间戳，浮点数形式，不需要参数
# c = time.time()
# print(c)

#得到的是格林尼治时间，将时间戳转为UTC时间元组
# t = time.gmtime(c)
# print(t)

#将时间戳转为本地时间元组
# b = time.localtime(c)
# print(b)

#将本地时间元组转为时间戳
# d = time.mktime(b)
# print(d)#省略小数点后的数



#将时间元组转成字符串
# s = time.asctime()
# print(s)
#Mon Jun 24 19:21:34 2019

#将时间戳转为字符串
# p = time.ctime(c)
# print(p)




#将时间元组转换成给定格式的字符串，参数2为时间元组，如果没有参数2，默认转当前时间
# q=time.strftime("%Y-%m-%d %X",b)
# print(q)
# print(type(q))

#将时间字符串转为时间元组
# w = time.strptime(q,"%Y-%m-%d %X")
# print(w)


#延迟一个时间，整型或浮点型
# time.sleep(2)


# 返回当前程序的cpu执行时间
# Unix系统始终返回全部的运行时间
# windows从第二次开始，都是以第一个调用此函数的开始时间戳作为基数
# time.clock()已经被弃用
# Deprecation Warning: time.clock has been deprecated in Python 3.3 and will be
# removed from Python 3.8: use time.perf_counter or time.process_time instead
# y1 = time.clock()
# print(y1)
# time.sleep(5)
# y2 = time.clock()
# print(y2)

#新的方式
#可以做性能测试
# y1 = time.perf_counter()
# print(y1)
# time.sleep(2)
# y2 = time.perf_counter()
# print(y2)
# time.sleep(2)
# y3 = time.perf_counter()
# print("%d" % y3)

'''
#测试运算速度
import time
sum1 = 0
time.perf_counter()
for i in range(100000000):
    sum1 += 1
print(time.perf_counter())
 
'''






