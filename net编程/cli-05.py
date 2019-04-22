import  socket

def tcp_clt():
    #1.建立通信 socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #2.请求和对方建立通路
    addr = ("127.0.0.1", 8998)
    sock.connect(addr)
    #3.发送内容到对方服务器
    msg = "I love xugaojuan"
    sock.send(msg.encode())

    #4.接受对方的反馈
    rst = sock.recv(500)
    print(rst.decode())
    # 5. 关闭链接通路
    sock.close()

if __name__ == '__main__':
    tcp_clt()