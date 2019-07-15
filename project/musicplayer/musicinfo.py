import tkinter
from tkinter import ttk
import time
import os
import pygame
import random
import sys



class MusicInfo(tkinter.Frame):
    def __init__(self,master,path):
        frame = tkinter.Frame(master)
        #0行1列
        frame.grid(row=0,column=1)

        self.path=path
        self.ev = tkinter.Variable()
        self.entry = tkinter.Entry(frame,textvariable = self.ev)
        self.entry.pack()



        self.buttonB = tkinter.Button(frame,text="<<",command=self.beforeMusic,width=3,height=1)
        self.buttonB.place(x=10,y=20)

        self.buttonStart = tkinter.Button(frame,text="Start",command=self.startMusic,width=3,height=1)
        self.buttonStart.pack()


        self.buttonN = tkinter.Button(frame,text=">>",command=self.nextMusic,width=3,height=1)
        self.buttonN.place(x=113,y=20)

        self.buttonStop = tkinter.Button(frame,text="Stop",command=self.stopMusic,width=3,height=1)
        self.buttonStop.place(x=10,y=50)

        self.buttonGo = tkinter.Button(frame,text="Go",command=self.goonMusic,width=3,height=1)
        self.buttonGo.pack(side=tkinter.TOP)

        self.buttonExit = tkinter.Button(frame,text="Exit",command=self.Exit,width=3,height=1)
        self.buttonExit.place(x=113,y=50)

        self.buttonrandomPlay = tkinter.Button(frame,text="Shuffle",command=self.randomPlay,width=5,height=1)
        self.buttonrandomPlay.pack()




    def beforeMusic(self):
        for fileName in os.listdir(self.path):
            #当前目录路径abs
            absPath = os.path.join(self.path,fileName)
            #判断是否是目录
            if os.path.isdir(absPath):
                self.beforeMusic(absPath)
            else:
                if self.entry.get():
                    pass



    def startMusic(self):
        absPath = os.path.join(self.path,self.entry.get())
        # print(absPath)
        pygame.mixer.init()
        #加载音乐
        pygame.mixer.music.load(absPath)
        #播放
        pygame.mixer.music.play()

        # time.sleep(30)
        #停止
        # pygame.mixer.music.stop()
    def stopMusic(self):
        pygame.mixer.music.pause()
    def goonMusic(self):
        pygame.mixer.music.unpause()
    def nextMusic(self):
        pass
    def Exit(self):
        sys.exit()
    def randomPlay(self):
        musics = [self.path+'\\'+music for music in os.listdir(self.path) if music.endswith('.mp3')]
        pygame.mixer.init()
        total =len(musics)
        if not pygame.mixer.music.get_busy():
            playMusic = random.choice(musics)
            pygame.mixer.music.load(playMusic)
            pygame.mixer.music.play()
        else:
            time.sleep(1)

