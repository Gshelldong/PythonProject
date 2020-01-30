#coding:utf-8
class Kwords():
    def __init__(self):
        self.MaxValue=0.9       # �ڴ� cpu Ӳ�̵����ʹ��ֵ 90%
        self.NormalValue=100     #�Ű���־���ղο�ֵ
        self.set_timeout=4          #��ʱʱ��
        self.jump_HostIp="61.128.196.123"        #����� IP
        self.jump_HostPort=1988                 #������˿�
        self.jump_HostUser='omc'                #������û���
        self.jump_HostPass='cQIsmsCu1@#'        #���������
        self.des_Ud_HostUser="ud"               #Ŀ�������û���
        self.des_Ud_HostPass='cQIsmsCu1@#'
        self.des_master_user="hadoop"
        self.des_master_pass='cQIsmsCu1@#'
        self.curre_username = "hadoop"
        self.ud_lists = ['cu-ud40','cu-ud45','cu-ud46','cu-ud50','cu-ud51','cu-ud52']
        self.master_lists = ["hadoop-master11","hadoop-master12","hadoop-master13",
                             "hadoop-master14","hadoop-master16","hadoop-master17",
                             "hadoop-master18"]
