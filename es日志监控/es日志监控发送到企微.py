import requests
import json
import time
import os

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S %p',
                    level=20)

def query_es(es_url, query_json, headers, timeout=10):
    query_json = json.dumps(query_json)
    try:
        res = requests.get(url=es_url, data=query_json, headers=headers, timeout=timeout)

        # es语句错误也会有返回但是状态码不是200
        if res.status_code != 200:
            logging.error("esl查询错误!")
            exit(1)

    except Exception as e:
        logging.error("请求es失败:", e)
        exit(1)

    slow_count = res.json()
    return slow_count


def get_slow_uri_count(res_query_es, slow_query_count = 100):
    """
    把es返回的json进行处理，返回uri 和 出现的次数
    :param res_query_es:
    :param slow_query_count:定义慢查询出现的次数，默认100
    :return:
    """
    slow_log_buckets = res_query_es.get('aggregations')["by_service"]["buckets"]
    uri_counts = []

    for slow_content in slow_log_buckets:
        if slow_content['doc_count'] >= slow_query_count:
            slow_uri_key = slow_content.get('key')
            slow_doc_count = slow_content.get('doc_count')
            uri_detail = "{} `{}`".format(slow_uri_key,slow_doc_count)
            uri_counts.append(uri_detail)

            # 只统计前面10条
            if len(uri_counts) >= 10:
                break

    return uri_counts


def generate_message(uri_counts: list) -> str:
    message_content = "### 5分钟内错误日志超过100条 \n>#### {}  \n \n#### 查看详情,点击[EKF](https://efk.ab.com/) ".format("\n>#### ".join(uri_counts))
    return message_content

def judge_token_expire(get_token):
    """
    缓存本地token信息,判断是否过期并返回access_token
    :param get_token:
    :return:
    """
    if not os.path.exists('run.tmp'):
        logging.info('本地token不存在，新建并缓存token')

        token_info = get_token()

        with open(r'run.tmp','w',encoding='utf-8') as f:
            json.dump(token_info, f)

        return token_info.get('access_token')

    else:
        with open(r'run.tmp','r',encoding='utf-8')as f:
            token_info = json.load(f)

        now_timestrap = int(time.time())

        token_generate_time = token_info.get('token_generate_time')
        expires_in = token_info.get('expires_in')

        # 如果现在的时间 - 生成时间 < (token过期时间 - 10 分钟)说明没过期，就直接返回
        if (now_timestrap - token_generate_time) < (expires_in - 600):
            return token_info.get('access_token')
        else:
            # 过期了久重新获取再重新写入
            token_info = get_token()

            with open(r'run.tmp', 'w', encoding='utf-8') as f:
                json.dump(token_info, f)

            return token_info.get('access_token')

class CompanyChatApp():
    def __init__(self,company_id,company_secret,agentid):
        self.company_id = company_id
        self.company_secret = company_secret
        self.agentid = agentid

        # 消息体
        self.template = {
           "touser" : "@all",
           "toparty" : "",
           "totag" : "totag",
           "agentid" : self.agentid,
           "safe":0,"enable_id_trans": 0,
           "enable_duplicate_check": 0,
           "duplicate_check_interval": 1800,
           "chatid": "CHATID",
           "msgtype":"markdown",
           "markdown": {
                "content": None
           }
        }

    @staticmethod
    def get_token():
        company_id = 'ww4d0b6'
        company_secret = 'wWODf27'
        request_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=" + company_id + "&corpsecret=" + company_secret
        res = requests.get(request_url, timeout=3)
        token_info = res.json()
        """
              token_info = {'errcode': 0,
             'errmsg': 'ok',
             'access_token': 'token_value',
             'expires_in': 7200}
        """
        token_info["token_generate_time"] = int(time.time())
        return token_info

    def send_message(self,access_token,message):
        send_message_url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=" + access_token
        self.template["markdown"]["content"] = message
        res = response = requests.post(send_message_url, data=json.dumps(self.template), headers=headers)
        if res.status_code == 200:
            logging.info('推送企业信息消息请求成功.')
            logging.info(response.json())  # 如果服务器返回JSON响应，可以调用response.json()解析响应数据
        else:
            logging.error('请求失败')
            logging.error('状态码：', response.status_code)
            logging.error('响应内容：', response.text)

# es查询部分
es_url = 'http://10.10.10.100:9200/java-java*/_search'
headers = {"Content-Type": "application/json"}
query_json = {"size": 0, "query": {"bool": {
    "must": [{"term": {"log.level": "ERROR"}}, {"range": {"@timestamp": {"gte": "now-5m/m", "lte": "now/m"}}}]}},
              "aggs": {"by_service": {"terms": {"field": "service.name", "order": {"_count": "desc"}}}}}


# 企业微信配置部分
company_id='ww4d0b'
company_secret='wWODf27a0'
agentid = 1000060

# 满足多少条查询就会发送消息
slow_query_count = 100

def run():
    res_query_es = query_es(es_url, query_json, headers)

    # slow_query_count 修改这个值可以修改匹配到的文档的次数
    uri_counts = get_slow_uri_count(res_query_es, slow_query_count=slow_query_count)

    if len(uri_counts) == 0:
        logging.info("没有符合条件的统计!")
        exit(1)

    # 生成发送的企业微信消息
    message = generate_message(uri_counts)

    # 获取token
    get_token = CompanyChatApp.get_token
    access_token = judge_token_expire(get_token)
    slow_log_alerter = CompanyChatApp(company_id,company_secret,agentid)

    # 发送消息
    slow_log_alerter.send_message(access_token, message)

if __name__ == '__main__':
    run()