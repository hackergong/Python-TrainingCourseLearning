#进程模块
import win32process

#系统
import win32con
import win32gui
import win32api
import ctypes

#进程权限，即系统标识，|这是位运算
PROCESS_ALL_ACCESS = (0x000F0000|0x00100000|0xFFF)

#找窗体
win = win32gui.FindWindow("MainWindow","植物大战僵尸")
#根据窗体找到进程号
hid,pid = win32process.GetWindowThreadProcessId(win)

#以最高权限打开进程
#pid为进程号
p = win32api.OpenProcess(PROCESS_ALL_ACCESS,False,pid)

#读数据应该用ctypes的类型，8位
data = ctypes.c_long()

#加载内核模块
md = ctypes.windll.LoadLibrary("C:\\Windows\\System32\\kernel32")

#读取内存
#311944712是游戏内存地址
md.ReadProcessMemory(int(p),311944712,ctypes.byref(data),4,None)
print("data = ",data)

#新值
newData = ctypes.c_long(10000)

#修改
md.WriteProcessMemory(int(p),311944712,ctypes.byref(newData),4,None)





















