# _*_ coding:UTf-8 _*_
# 开发团队 ：jonty
# 开发人员 ：jonty
# 开发时间 ：2020/4/17 14:38
# 文件名称 ：2、TCP编程.py
# 开发工具 ：PyCharm

import socket  # 导入模块

host = socket.gethostname()  # 主机IP
port = 32151  # 端口号
web = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建socket对象
web.bind((host, port))  # 绑定端口
web.listen(5)  # 启动监听设置连接数
sock, addr = web.accept()  # 被动接收TCP客户端连接
print('连接已建立')
info = sock.recv(1024).decode()  # 接收客户端数据
while info != 'Bye':
    if info:
        print("接收到的内容：", info)
    send_data = input("输入发送的内容：\n")  # 发送消息
    sock.send(send_data.encode())  # 发送TCP数据
    if send_data == "Bye":  # 如果发送Bye则退出
        break
    info = sock.recv(1024).decode()  # 接收客户端数据
sock.close()  # 关闭客户端套接字
web.close()  # 关闭 服务器套接字

# while True:
#     conn, addr = web.accept()  # 建立客户端连接
#     data = conn.recv(1024)  # 获取客户端请求的数据
#     print(data)  # 打印接收数据
#     conn.sendall(b'HTTP/1.1 200 OK \r\n\r\nHello World')
#     conn.close()
