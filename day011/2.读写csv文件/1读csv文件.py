import csv


def readCsv(path):
    infoList = []
    with open(path,"r") as f:
        allFileInfo = csv.reader(f)
        print(allFileInfo)
        for row in allFileInfo():
            infoList.append(row)
    return infoList

info = readCsv(r"path")
































































