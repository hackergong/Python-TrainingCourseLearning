import tkinter
import socket
import threading

win = tkinter.Tk()
win.title("Server")
win.geometry("400x400+200+20")

users = {}

def run(ck,ca):

    userName = ck.recv(1023)
    users[userName.decode("utf-8")] = ck
    print(users)
    # printStr =  userName + "connect"
    # text.insert(tkinter.END,printStr)
    while True:
        rData = ck.recv(1024)
        dataStr = rData.decode("utf-8")
        infoList = dataStr.split(":")
        users[infoList[0]].send((userName.decode("utf-8") + ":" + infoList[1]+"\n").encode("utf-8"))

def start():
    ipStr = eip.get()
    eportStr = eport.get()

    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((ipStr,int(eportStr)))
    server.listen(10)
    str="服务器启动成功"
    text.insert(tkinter.INSERT,str)
    while True:
        ck,ca = server.accept()
        t = threading.Thread(target=run,args=(ck,ca))
        t.start()

def startServer():
    s = threading.Thread(target=start)
    s.start()



labelIp = tkinter.Label(win,text="ip").grid(row=0,column=0)
labelPort = tkinter.Label(win,text="port").grid(row=1,column=0)

eip = tkinter.Variable()
eport = tkinter.Variable()
entryIp = tkinter.Entry(win,textvariable=eip).grid(row=0,column=1)
entryPort = tkinter.Entry(win,textvariable=eport).grid(row=1,column=1)

buttonStart = tkinter.Button(win,text="启动",command=startServer,width=5,height=1).grid(row=2,column=1)

text = tkinter.Text(win,width=30,height=20)
text.grid(row=3,column=0)




win.mainloop()