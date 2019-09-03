class Kwords():
    def __init__(self):
        self.MaxValue=0.9       #  内存 cpu 硬盘的最大使用值 90%
        self.NormalValue=100     #信安日志快照参考值
        self.set_timeout=4         #超时时间
        self.jump_HostIp=""        #跳板机 IP
        self.jump_HostPort=                #跳板机端口
        self.jump_HostUser=''                #跳板机用户名
        self.jump_HostPass=''        #跳板机密码
        self.des_Ud_HostUser=""               #目标主机用户名
        self.des_Ud_HostPass=''
        self.des_master_user=""
        self.des_master_pass=''
        self.curre_username = ""
        self.ud_lists = ['cu-ud40','cu-ud45','cu-ud46','cu-ud50','cu-ud51','cu-ud52']
        self.master_lists = ["hadoop-master11","hadoop-master12","hadoop-master13",
                             "hadoop-master14","hadoop-master16","hadoop-master17",
                             "hadoop-master18"]
