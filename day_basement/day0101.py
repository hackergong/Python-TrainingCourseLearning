import time

musicstr="""[00:00.03]* oh 喜欢你~
[00:04.30]你是那么的让我安心
[00:08.28]oh 喜欢你1~
[00:12.36]再没有什么把你代替
[00:16.44]oh 喜欢你2~
[00:19.22]一见你怎能保持清醒
[00:24.71]目眩又神迷 在我的心里
[00:28.79]只喜欢你
[00:38.93]和你一起不会在意世界的无理
[00:46.94]静静靠着你 把烦恼丢得远远的
[00:55.38]和你一起空气变得特别的清新
[01:03.60]听你的呼吸 随着你 思想中飞行
[01:13.84]* oh 喜欢你3~
[01:17.98]你是那么的让我安心
[01:22.11]oh 喜欢你4~
[01:26.10]再没有什么把你代替
[01:30.28]oh 喜欢你5~
[01:33.00]一见你怎能保持清醒1
[01:38.60]目眩又神迷 在我的心里1
[01:42.64]只喜欢你1"""
musiclrclist=musicstr.splitlines()

lrcDict={}   #创建一个字典
for Ircline in musiclrclist:
    Irclinelist=Ircline.split("]")
    #print(Irclinelist)
    for index in range(len(Irclinelist)-1):
        #print(index)#因为分割后为两个部分，所以下标为0,1，而此时len的长度为2，若直接输出则会将歌词显示
        timestr=Irclinelist[index][1:]
        #print(timestr)
        timelist = timestr.split(":")
        time1 = float(timelist[0])*60 + float(timelist[1])
        #print(time)

        lrcDict[time1] = Irclinelist[-1]

allTimeList = []
for t in lrcDict:
    allTimeList.append(t)
    allTimeList.sort()

#print(allTimeList)

# while 1:
#     getTime = float(input("请输入一个时间"))
#
#     for n in range(len(allTimeList)):
#         tempTime = allTimeList[n]
#         if getTime < tempTime:
#             break
#     if n == 0:
#         print("时间太小")
#     else:
#         print(lrcDict[allTimeList[n-1]])
getTime=0
while 1:
    for n in range(len(allTimeList())):
        tempTime = allTimeList[n]
        if getTime < tempTime:
            break
    lrc = lrcDict.get(allTimeList[n-1])
    if lrc == None:
        pass
    else:
        print(lrc)
    time.sleep(2)
    getTime +=1