#coding:utf-8
from jumpssh import SSHSession
import jumpssh
import inspect_cmd
import time
import inspect_func
from inspect_words import Kwords


kwords = Kwords()

inspect_hosts_dict = []
today_slaverlist = []
slaver_list=[]

ud_lists = kwords.ud_lists
master_lists = kwords.master_lists

inspect_ud ,inspect_master ,inspect_slaver = inspect_func.input_select() #选择巡检哪些主机
if inspect_slaver:   # 如果inspect_slaver 返回的是True
    slaver_list=inspect_func.create_slaver_namelist(today_slaverlist)
hosts_dict = inspect_func.create_inspect_dict(inspect_hosts_dict,slaver_list,inspect_ud,inspect_master,inspect_slaver)

# print(hosts_dict);print(slaver_list)

try:
    jump_server = SSHSession(kwords.jump_HostIp, kwords.jump_HostUser, port=kwords.jump_HostPort,  #连接跳板机
                         password=kwords.jump_HostPass).open()
except Exception as e:
    print(e)
inspectcmd = inspect_cmd.InspectCmd();cmdLists = inspectcmd.cmd_lists  # 生成巡检命令列表


for ip in hosts_dict.keys():  # 主程序

    print("正在连接 ",ip,".....")
    if hosts_dict[ip] in ud_lists:   #判断哪个主机用那个主机名
        des_username = kwords.des_Ud_HostUser
    else:
        des_username = kwords.curre_username

    a = inspect_func.RemoteHost_IsActive(jump_server, ip, des_username, kwords.des_Ud_HostPass) #判断主机是否可连接 正常返回True
    if a != True:
        with open("inspect_log.log", "a") as f:
            f.write("IP {0} 主机异常\n".format(ip))
            print("IP:{0} 主机异常，连接超时".format(ip))
        continue


    try:  #连接目标主机
        des_remote = jump_server.get_remote_session(ip, username=des_username, password=kwords.des_Ud_HostPass,
                                                retry=1, retry_interval=5)
    except Exception as e:
        print(e)
        des_remote.close()
        continue

    try:
        if hosts_dict[ip] == ud_lists[0]:  # 判断是Ud哪台服务器40
            print("正在巡检: " + hosts_dict[ip], end=" ")
            udList_1 = [cmdLists[0], cmdLists[10], cmdLists[11], cmdLists[12], cmdLists[5]]  # 用于巡检Ud的命令
            inspect_func.inspect_ud40(udList_1, " ", des_remote)
            print("     Done.")

        if hosts_dict[ip] in ud_lists[1:3]:  # 判断是Ud哪台服务器45\46
            print("正在巡检: " + hosts_dict[ip], end=" ")
            udList_1 = [cmdLists[0], cmdLists[10], cmdLists[11], cmdLists[12], cmdLists[1], cmdLists[2], cmdLists[3],
                        cmdLists[4]]  # 用于巡检Ud的命令
            inspect_func.inspect_ud45_ud46(udList_1, des_remote)
            print("     Done.")

        if hosts_dict[ip] in ud_lists[3:6]:  # 判断是Ud哪台服务器50\51\52
            print("正在巡检: " + hosts_dict[ip], end=" ")
            udList_1 = [cmdLists[0], cmdLists[10], cmdLists[11], cmdLists[12], cmdLists[1], cmdLists[2], cmdLists[3],
                        cmdLists[4]]  # 用于巡检Ud的命令
            inspect_func.inspect_ud50_ud52(udList_1, des_remote)
            print("     Done.")

        if hosts_dict[ip] in master_lists[0:3]:  # namenode
            print("正在巡检: " + hosts_dict[ip], end=" ")
            master_cmd_lists = [cmdLists[0], cmdLists[10], cmdLists[11], cmdLists[12], cmdLists[1], cmdLists[6]]
            '''主机名 内存 CPU 存储 hadoop使用率'''
            inspect_func.inspect_namenode(master_cmd_lists, des_remote)
            print("     Done.")

        if hosts_dict[ip] in master_lists[3:7]:  # redis
            print("正在巡检: " + hosts_dict[ip], end=" ")
            master_cmd_lists = [cmdLists[0], cmdLists[10], cmdLists[11], cmdLists[12], cmdLists[7]]
            inspect_func.inspect_redis(master_cmd_lists, des_remote)
            print("     Done.")

        if not inspect_func.mate_key(hosts_dict[ip]):
            print("正在巡检: " + hosts_dict[ip], end=" ")
            datanode_cmd_lists = [cmdLists[0], cmdLists[10], cmdLists[11], cmdLists[12], cmdLists[7]]
            inspect_func.inspect_datanode(datanode_cmd_lists, des_remote)
            print("     Done.")

    except Exception as e:
        print(e," 主机返回数据异常请手动检查")
        with open("inspect_log.log", "a") as f:
            f.write("主机返回数据异常请手动检查\n")
        continue
    des_remote.close()

jump_server.close()
print("巡检完成！！！")