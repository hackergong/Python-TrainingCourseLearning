import tkinter
import socket
import threading

win = tkinter.Tk()
win.title("chat")
win.geometry("400x400+200+20")

#输入用户名，ip，port，点击登录
#聊天界面，好友，输入文字界面，发送
ck = None

def getInfo():
    while True:
        data = ck.recv(1024)
        text.insert(tkinter.INSERT,data.decode("utf-8"))



def connectServer():
    global ck
    ipStr = eip.get()
    portStr = eport.get()
    userStr = euser.get()
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((ipStr,int(portStr)))
    client.send(userStr.encode("utf-8"))
    ck = client
    #等待接收数据
    t = threading.Thread(target=getInfo)
    t.start()

def sendMessage():
    friend = efriend.get()
    sendStr = esend.get()
    sendStr = friend + ":" + sendStr + "\n"

    ck.send(sendStr.encode("utf-8"))



labelUser = tkinter.Label(win,text="User").grid(row=0,column=0)
euser = tkinter.Variable()
entryUser = tkinter.Entry(win,textvariable=euser).grid(row=0,column=1)

labelIp = tkinter.Label(win,text="ip").grid(row=1,column=0)
eip = tkinter.Variable()
entryIp = tkinter.Entry(win,textvariable=eip).grid(row=1,column=1)

labelPort = tkinter.Label(win,text="port").grid(row=2,column=0)
eport = tkinter.Variable()
entryPort = tkinter.Entry(win,textvariable=eport).grid(row=2,column=1)

button =tkinter.Button(win,text="连接",command=connectServer).grid(row=3,column=1)


text = tkinter.Text(win,width=30,height=10)
text.grid(row=4,column=0)

esend = tkinter.Variable()
entrySend = tkinter.Entry(win,textvariabl=esend).grid(row=5,column=0)

efriend = tkinter.Variable()
entryFriend = tkinter.Entry(win,textvariabl=efriend).grid(row=6,column=0)

buttonSend = tkinter.Button(win,text="发送",command=sendMessage).grid(row=6,column=1)








win.mainloop()