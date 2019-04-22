import socket

#模拟服务器的函数
def serverFunc():
    #建立socket

    #socket.AF_INET: 使用ipv4协议族
    #socket.SOCK_DGRAM:使用UDP通信
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #2.绑定IP和port
    #127.0.0.1 :ip地址表示机器本身
    #7852  ：表示指定端口号
    #地址是一个tuple类型，(ip, port)
    addr = ("127.0.0.1", 7852)
    sock.bind(addr)


    # # 接受对方消息
    # 等待方式为死等， 没有其他可能性
    # recvfrom接受的返回值是一个tuple，前一项表示数据，后一项表示地址
    # 500参数的含义是缓冲区大小
    # rst = sock.recvfrom(500)
    data , addr =sock.recvfrom(500)

    # 发送过来的数据是bytes格式，必须通过解码才能得到str格式内容
    # decode默认参数是utf8
    text = data.decode()
    print(type(text))
    print(text)

    #给对方返回的消息
    rsp = "我不饿！"

    #发送的消息要编码成bytes格式
    #默认是utf8
    data = rsp.encode()
    sock.sendto(data, addr)

if __name__ == '__main__':
    import time
    while 1:
        try:
            serverFunc()
        except Exception as e:
            print(e)

        time.sleep(1)


