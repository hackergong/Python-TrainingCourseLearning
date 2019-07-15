
#regedit->HKEY_CURRENT_USER->Control Panel->Desktop->WallPaper

import win32api
import win32con
import win32gui
import time
import os

class musicWallPaper(object):
    def setWallPaper(path):
    #
        reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
    #2拉伸  0居中，6适应  10填充
        win32api.RegSetValueEx(reg_key,"WallpaperStyle",0,
             win32con.REG_SZ,"6")
    #
    #立即生效SPIF_SENDWININICHANGE
    # win32api.RegSetValueEx(reg_key,"WallPaper")
        win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,
                                  path,win32con.SPIF_SENDWININICHANGE)
    path = r"H:\Wallpaper\car"
    while True:
        for list in os.listdir(path):
            setWallPaper(os.path.join(path,list))
            time.sleep(2)

