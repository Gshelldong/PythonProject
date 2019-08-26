import pyperclip

def put_clip(input_txt):
    pyperclip.copy(input_txt)
    pyperclip.paste()

def creat_hostnames(hosts_names):
    for i in range(892, 981):                 #生成主机名 hadoop-slaver892 - 981
        host_name = "hadoop-slaver" + str(i)
        hosts_names.append(host_name)

