'''
- Client端流程
            1. 建立通信的socket
            2. 发送内容到指定服务器
            3. 接受服务器给定的反馈内容
'''
import socket

def clientFunc():
    # 1. 建立socket
    # socket.AF_INET:使用ipv4协议族
    # socket.SOCK_DGRAM: 使用UDP通信
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    text = "I love xuaojuan "

    #发送的形式是bytes格式
    data = text.encode()

    #发送
    sock.sendto(data, ("127.0.0.1", 7852))

    data, addr = sock.recvfrom(200)
    data = data.decode()

    print(data)

if __name__ == '__main__':
    clientFunc()