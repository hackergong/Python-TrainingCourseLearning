import calendar

'''
日历模块
'''


#使用
#返回指定某年某月的日历
# print(calendar.month(2019,7))

#返回指定年的 日历
# print(calendar.calendar(2017))

#闰年返回True，否则返回False
# print(calendar.isleap(2000))

#返回某年某月的weekday的第一天和天数
# print(calendar.monthrange(2019,7))

#返回某个月以每一周为元素的列表
print(calendar.monthcalendar(2019,6))


