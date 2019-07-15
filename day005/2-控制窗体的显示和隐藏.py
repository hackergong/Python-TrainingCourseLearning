#
import win32con

import win32gui

import time

#找出窗体的编号
# WeChatWin = win32gui.FindWindow("TXGuiFoundation","WeChat")

#隐藏窗体
# win32gui.ShowWindow(WeChatWin.win32con.SW_HIDE)
# win32gui.ShowWindow(WeChatWin.win32con.SW_SHOW)

# time.sleep(2)
#
#显示窗体
# win32gui.ShowWindow(WeChatWin.win32con.SW_SHOW)

#实现循环操作
while True:
    WeChatWin = win32gui.FindWindow("TXGuiFoundation","WeChat")
    win32gui.ShowWindow(WeChatWin.win32con.SW_HIDE)
    time.sleep(1)
    win32gui.ShowWindow(WeChatWin.win32con.SW_SHOW)
    time.sleep(1)




























































































