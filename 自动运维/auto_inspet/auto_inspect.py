import pyautogui
import pyperclip
import inpect_cmd
import inspect_fun
from time import sleep
pyautogui.FAILSAFE = True

"""
基于图形界面，模拟的是键盘敲击和鼠标运动，服务器延迟返回程序也会继续运行；如有异常把鼠标 移动至屏左上角，
全屏模式 下易于操作
"""

hosts_names = []
inspect_fun.creat_hostnames(hosts_names)  #生成主机列表

pyautogui.moveTo(200, 730, duration=0.2)
pyautogui.click()                           #移动鼠标到位置（200, 730） 点击一下
IputCmd = inpect_cmd.InspectCmd()


for host in hosts_names:
    ssh_host = "ssh hadoop@" + host
    print(ssh_host)

    inspect_fun.put_clip(ssh_host)  #把生成的主机名放到剪切板中
    pyautogui.hotkey('ctrl', 'v')   # ctrl +v
    sleep(0.4)                      #延迟 0.4s
    pyautogui.press("\n")
    pyautogui.write("cQIsmsCu1@#",interval=0.03) #interval 输入每个字符的间隔 s
    pyautogui.press("\n")                        # 回车

    IputCmd.cmd_input()
    sleep(1.5)







