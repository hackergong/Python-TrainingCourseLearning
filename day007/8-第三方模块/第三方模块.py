'''
#安装第三方模块
#今天不是讲第三方模块怎么使用，而是讲如何使用第三方模块。

#通过命令指示符终端

Mac:无需安装
Linux:无需安装
window:勾选了pip和Add python.exe to path

'''

'''
安装第三方模块，需要知道模块的名字
pip --version
pillow  非常强大的处理图像的工具库
pip install Pillow
如果报错 pip install --upgrade pip

pip -V  查看pip版本，以及pip目录
print(sys.path)

'''
from PIL import Image

#打开图片
im = Image.open("lena.tif")
#信息，大小，类型
print(im.format,im.size,im.mode)
#设置图片的大小
im.thumbnail((150,150))
#保存为新图片
im.save("tem.jpg","JPEG")


























