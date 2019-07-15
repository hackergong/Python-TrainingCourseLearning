'''
win+R 输入control-----即打开控制面板
'''

#系统客户端
import win32com.client
import time

tracy = win32com.client.Dispatch("SAPI.SPVOICE")

while 1:
    tracy.Speak("I like play basketball")
    time.sleep(5)