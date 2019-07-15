#有序字典
from collections import OrderedDict
#读取数据   只能写xls
from pyexcel_xls import save_data

def makeExcelFile(path,data):
    dic = OrderedDict()
    for sheetName,sheetValue in data.items():
        d = {}
        d[sheetName] = sheetValue
        dic.update(d)

    save_data(path,dic)


path = r"G:\python_learn\pycharm_learn\pythonlearn\day011\5.excel自动化办公\a.xls"
makeExcelFile(path,{"表1":[[1,2,3],[4,5,6],[7,8,9]],"表2":[[11,12,13],[14,15,16],[17,18,19]]})








