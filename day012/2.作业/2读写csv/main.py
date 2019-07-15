from dealFile import DealFile


d = DealFile()

toPath = r"G:\python_learn\pycharm_learn\pythonlearn\day012\2.作业\2读写csv\tracy.csv"


for i in range(1,4):
    path = r"G:\python_learn\pycharm_learn\pythonlearn\day012\2.作业\2读写csv\0000"+str(i)+".csv"
    listInfo = d.readCsv(path)
    d.writeCsv(toPath,listInfo)

allInfo = d.readCsv(toPath)
print(allInfo)