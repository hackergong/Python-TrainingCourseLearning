"""
:param
    无
:return
    无
功能：调用笔记本摄像头获取视频图片
"""""


import numpy as np
import cv2
#调用笔记本内置摄像头，所以参数为0，如果有其他的摄像头可以调整参数为1，2
cap=cv2.VideoCapture(0)
# sucess,img=cap.read()
# cv2.imshow(img)

while True:
    #从摄像头读取图片
    img,success=cap.read()
    #转为灰度图片
   # gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #显示摄像头，背景是灰度。
    cv2.imshow("img",success)
    #保持画面的持续。
    k=cv2.waitKey(1)
    if k == 27:
        #通过esc键退出摄像
        cv2.destroyAllWindows()
        break
    elif k==ord("s"):
        #通过s键保存图片，并退出。
        cv2.imwrite("image2.jpg",img)
        cv2.destroyAllWindows()
        break

while True:
    m = input("输入0退出")
    if  m=="0":
        cap.release()




'''
import cv2
import numpy as np#添加模块和矩阵模块
cap=cv2.VideoCapture(0)
#VideoCapture-视频捕获
#打开摄像头，若打开本地视频，同opencv一样，只需将０换成("×××.avi")
while(1):    # get a frame
    ret, frame = cap.read()    # show a frame
    cv2.imshow("capture", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
#释放并销毁窗口
'''