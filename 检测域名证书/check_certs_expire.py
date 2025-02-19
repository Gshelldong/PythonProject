# coding: utf-8
import json
import time

from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkdns.v2.region.dns_region import DnsRegion
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkdns.v2 import *
from datetime import datetime,timedelta
import socket
import ssl
from openpyxl import Workbook
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor,Future

# 定义华为云的认证信息ak,sk
ak = '1111'
sk = '222'

# 域名的zone_id
zone_ids = {'aa.com': 'ff8080827f40',
           'bb.com': 'ff8080827f4',
           'cc.com': 'ff8080827'}

def export_dns_record(zone_id):
    credentials = BasicCredentials(ak, sk)

    client = DnsClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(DnsRegion.value_of("cn-south-1")) \
        .build()
    try:
        request = ListRecordSetsByZoneRequest()
        request.zone_id = zone_id
        request.status = "ACTIVE"
        # request.limit=5 限制最大返回条数，调试用，默认返回500条
        response = client.list_record_sets_by_zone(request)
        names_records = str((response.recordsets))  # 这个方法可以重写父类中的方法，让json.dump支持不能够序列化的内容，比如时间
        with open('names-record.json',mode='w',encoding='utf-8') as f:
            json.dump(names_records,f)
        f.close()

    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)
        print('请检查华为云认证配置')
        exit(1)

def check_certs_expire(cert_notafter):
    # 定义日期格式，注意两个空格和GMT部分
    date_format = "%b  %d %H:%M:%S %Y GMT"

    # 使用strptime()方法解析日期字符串
    notafter_day = datetime.strptime(cert_notafter, date_format)

    # 证书过期时间检查
    check_day = timedelta(days=15)
    # 现在时间
    now_day = datetime.today()
    # 剩余时间
    remaining_time = notafter_day - now_day

    if remaining_time < check_day:
        return '证书即将过期请检查'
    else:
        return str(remaining_time)

def get_cert_info(host_record): # 主机记录
    """
    这个函数域名证书的subject和commonname证书得到并返回
    :return:
    """
    # 设置socket的超时时间为5秒
    socket.setdefaulttimeout(3)
    socket.timeout(3)
    # 创建默认的SSL上下文
    context = ssl.create_default_context()
    # 创建一个SSL套接字
    try:
        skt = context.wrap_socket(socket.socket(), server_hostname=host_record)
        skt.connect((host_record, 443))
        cert_res = skt.getpeercert()
        subject = cert_res['subject']
        notafter = cert_res['notAfter']
        skt.close()
        return subject,notafter
    except (socket.timeout, ConnectionRefusedError, socket.error) as e:
        return {'messages': str(e)}
# 从证书中获取到颁发组织的名称
def get_commonname(cert_subject: tuple) -> str:
    """
    :param cert_subject: 证书的subject.
    :return: 证书颁发的目的组织,就是主域名.
    """
    subject_info = {}
    for common in cert_subject:
        for content in common:
            subject_info.update(dict([content]))
    commonname = subject_info.get('commonName')
    return commonname

def write_xlsx(inspect_resouts:list) -> None:
    # 写表格
    wb = Workbook()
    ws = wb.active

    for res in inspect_resouts:
        ws.append(res)

    wb.save("result.xlsx")
    wb.close()

def select_dic(dict_data):
    index = 1
    select_options = dict()
    print('请选择要巡检域名的编号:')
    for i in dict_data.keys():
        select_p = str(index)
        print(index,' -> ',i)
        select_options[select_p] = i
        index +=1
    choice = input(">>>: ").strip()
    return select_options.get(choice)

def task1(name_record):
    certs_inspect = []  # 每个主机记录的信息记录一个列表
    host_record = name_record['name'].rsplit('.', 1)[0]
    certs_inspect.append(host_record)
    get_cert_info_res = get_cert_info(host_record)
    # print(get_cert_info_res)
    if type(get_cert_info_res) is dict:  # 检测有异常置空
        # 表格的占位
        certs_inspect.extend(['-', '-', '-'])
        certs_inspect.append(get_cert_info_res.get('messages'))
    else:
        commonName, cert_notafter = get_cert_info_res
        commonName = get_commonname(commonName)
        certs_inspect.append(commonName)
        check_certs_expire_res = check_certs_expire(cert_notafter)
        certs_inspect.append(check_certs_expire_res)
        certs_inspect.append(cert_notafter)
    print('巡检记录: %s'%host_record)
    certs_inspect_res.append(certs_inspect)  # 把每次处理的结果都放到汇总的列表中去

if __name__ == '__main__':

    print("""
        欢迎使用域名证书巡检程序.
        auther: gongxiaoliao
        mail: gongxiaoliao@kailinjt.com
        date: 2024-12-16.
        
        巡检结果请查看运行目录下resault.xlsx
    """)

    # 巡检之后的结果，带表头
    certs_inspect_res = [['域名记录', '绑定证书', '剩余时间', '到期时间','巡检信息'],]

    # 获取域名在华为云的id
    choice_domain = select_dic(zone_ids)
    zone_id = zone_ids.get(choice_domain)

    # 导出华为云的dns解析记录
    export_dns_record(zone_id)

    # 读取华为云导出的dns记录
    with open('names-record.json', mode='r', encoding='utf-8') as f:
        res = json.loads(f.read())
        name_records = json.loads(res)

    pool = ThreadPoolExecutor(20)  # 括号内可以传参数指定线程池内的线程个数

    for name_record in name_records:
        res  = pool.submit(task1, name_record)
        # print(res.result()) # 如果task1 函数没有返回值这里就不会有结果
    pool.shutdown()

    try:
        write_xlsx(certs_inspect_res) # 最后写入表格
    except PermissionError as e:
        print('写入表格错误，请检查表格是否正在被打开!')
    finally:
        input('\n巡检完成,按任意键退出!')
