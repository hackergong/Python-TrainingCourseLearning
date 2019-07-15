
import time
import pygame

import win32api
import win32con
import win32gui
import time
import os
#线程模块
import threading

path = r"G:\python_learn\pycharm_learn\pythonlearn\day011\9.整蛊小程序\music"
def go():
    pygame.mixer.init()
    while True:
        for list in os.listdir(path):
            filePath = os.path.join(path,list)
            track = pygame.mixer.music.load(filePath)
            pygame.mixer.music.play()
            time.sleep(10)
            pygame.mixer.music.stop()


def setWallPaper(path):
    reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(reg_key,"WallpaperStyle",0,
             win32con.REG_SZ,"6")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,
                                  path,win32con.SPIF_SENDWININICHANGE)

th =threading.Thread(target=go,name="LoopThread")
th.start()
while True:
    for i in range(8):
        filePath = r"G:\python_learn\pycharm_learn\pythonlearn\day011\9.整蛊小程序\res"+"\\"+str(i)+".jpg"
        setWallPaper(filePath)
        time.sleep(2)

