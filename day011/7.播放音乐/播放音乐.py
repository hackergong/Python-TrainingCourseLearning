#pip install pygame

import time
import pygame

#播放音乐的路径
filePath = r"G:\python_learn\pycharm_learn\pythonlearn\day011\7.播放音乐\res\demo2.mp3"

#初始化
pygame.mixer.init()

#加载音乐
track = pygame.mixer.music.load(filePath)

#播放
pygame.mixer.music.play()
#暂停
time.sleep(30)
# pygame.mixer.music.pause()  #暂停但不结束
#停止
pygame.mixer.music.stop()


#作业音乐播放器

