import tkinter
from tkinter import ttk
import os
from musicWin import MusicWin
from musicinfo import MusicInfo
from musicwallpaper import musicWallPaper
import threading

win = tkinter.Tk()
win.title("MusicPlayer")
win.geometry("500x500+200+50")

path=r"G:\CloudMusic"


infoWin= MusicInfo(win,path)
musicplayerwin = MusicWin(win,path,infoWin)

th =threading.Thread(target=musicWallPaper,name="LoopThread")
th.start()


win.mainloop()