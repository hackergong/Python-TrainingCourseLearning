import tkinter
from tkinter import ttk
import os
from treewindows import TreeWindows
from infowindows import InfoWindows


win = tkinter.Tk()
win.title("作业1")
win.geometry("500x400+200+50")

path=r"G:\python_learn\pycharm_learn\pythonlearn"

infoWin = InfoWindows(win)
treeWin = TreeWindows(win,path,infoWin)

win.mainloop()
























