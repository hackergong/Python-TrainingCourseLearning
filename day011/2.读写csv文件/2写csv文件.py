import csv

def writeCsv(path,data):
    with open(path,"w") as f:
        writer = csv.writer(f) #创建一个writer
        for rowData in data:
            writer.writerow(rowData)  #按行写入


path = r"G:\python_learn\pycharm_learn\pythonlearn\day011\2.读写csv文件\00003.csv"

writeCsv(path,[["111","112","113"],["141","151","611"],["171","118","119"]])









