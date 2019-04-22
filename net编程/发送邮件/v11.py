from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

head_from=Header("测试文件<1402122292@qq.com>")
#构建一个MIMEMultipart
msg = MIMEMultipart("alternative")
header_from = Header("从本地发出去的邮件<1402122292@qq.com>", "utf-8")
msg['From'] = header_from

#接收者信息
header_to = Header("<去的各种地方>","utf-8")
msg['From']= header_to

header_sub = Header("这是邮件的主题", "utf-8")
msg['Subject'] = header_sub

#构建HTML内容
html_content = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Title</title>
            </head>
            <body>
            <h1> 这是一封HTML格式邮件</h1>
            </body>
            </html>
        """
msg_html = MIMEText(html_content, "html", "utf-8")
msg.attach(msg_html)

msg_text =MIMEText("Just text content", "plain","utf-8")
msg.attach(msg_text)

#发送email地址，此处地址直接使用我的qq有偶像，密码一般需要临时输入，此处偷懒
from_addr = "1402122292@qq.com"
#此处密码是经过申请设置后的授权码，不是你的qq邮箱密码
from_pwd= "yzwvuvmjffrahiib"
# 收件人信息
# 此处使用qq邮箱，我给自己发送
to_addr = ["1402122292@qq.com","2395744154@qq.com"]

# 输入SMTP服务器地址
# 此处根据不同的邮件服务商有不同的值，
# 现在基本任何一家邮件服务商，如果采用第三方收发邮件，都需要开启授权选项
# 腾讯qq邮箱所的smtp地址是 smtp.qq.com
smtp_srv = "smtp.qq.com"

try:
# 两个参数
# 第一个是服务器地址，但一定是bytes格式，所以需要编码
# 第二个参数是服务器的接受访问端口
    import smtplib
    srv = smtplib.SMTP_SSL(smtp_srv.encode(),465) #SMTP协议默认端口25
    #登录邮箱发送
    srv.login(from_addr, from_pwd)
    # 发送邮件
    # 三个参数
    # 1. 发送地址
    # 2. 接受地址，必须是list形式
    # 3. 发送内容，作为字符串发送
    for i in to_addr:
        srv.sendmail(from_addr,[i],msg.as_string())
    srv.quit()
    print("邮件发送成功---------")
except Exception as e:
    print(e)
