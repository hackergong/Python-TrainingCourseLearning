import win32con
import win32api
import time

#设置鼠标的位置
win32api.SetCursorPos([90,10])
time.sleep(0.1)

#鼠标左键按下
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0)
#鼠标右键按下
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)





#介绍API函数的中文帮助文档