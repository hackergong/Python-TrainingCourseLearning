#有序字典
from collections import OrderedDict

#读取数据   只能写xls
from pyexcel_xls import get_data


def readXlsAndXlsxFile(path):
    dic = OrderedDict()
    #抓取数据
    xdata = get_data(path)
    for sheet in xdata:
        dic[sheet] = xdata[sheet]
    return dic

path = r"G:\python_learn\pycharm_learn\pythonlearn\day011\5.excel自动化办公\tracy1.xlsx"

dic = readXlsAndXlsxFile(path)
print(dic)
print(len(dic))

