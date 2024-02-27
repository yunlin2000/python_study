"""
日常娱乐/办公经常遇到一开机就得启动好几个软件,输入好几次账号密码.久了/多了,就很麻烦.所以运用Python知识,实现一个自动登录脚本.
思路:
    1.通过图标/指令启动程序
    2.选中输入框
    3.输入数据
    4.重复2/3操作,直到完成所有输入内容
    5.点击登录

项目名称:自动登录
项目描述:通过Windows编程里的识图机制/模拟鼠标键盘操作实现自动登录.
项目环境:Pycharm && pywin32 && pyautogui(后两模块需专门下载)
作者所属:霖老

工具下载指令--安装Python环境后,在CMD(或Pycharm终端)中
pip install pywin32 --default-timeout=100 -i https://pypi.tuna.tsinghua.edu.cn/simple/
pip install pyautogui --default-timeout=100 -i https://pypi.tuna.tsinghua.edu.cn/simple

本案例需要一定Python基础,还看不懂不影响.先把思路学好,后续基础扎实了再来还原.
"""

# 1.准备工具
import time

import win32api as api

# 2.启动应用程序
# 通过图标识图--让Python程序找到程序图标并点击图标
# qq = pgui.locateOnScreen('qq.png')
# print(qq)
# pgui.doubleClick(qq)
# time.sleep(3)

# 通过指令，直接启动
qq = r"C:\Program Files (x86)\Tencent\QQ\Bin\QQScLauncher.exe"
api.ShellExecute(None, "runas", qq, "","",1)
# api.ShellExecute(0, 'open', qq, None, None, 1)

# os.system(qq)
time.sleep(2)
# 3.查找用户文本框，输入用户名（号码）
# qq = pgui.locateOnScreen('qq.png')
# print(qq)
# time.sleep(3)
# pgui.doubleClick(qq)
