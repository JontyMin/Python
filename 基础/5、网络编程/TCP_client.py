# _*_ coding:UTf-8 _*_
# 开发团队 ：jonty
# 开发人员 ：jonty
# 开发时间 ：2020/4/17 14:46
# 文件名称 ：TCP_client.py
# 开发工具 ：PyCharm

# import socket
# s = socket.socket()
# host = '192.168.120.188'  # 主机IP
# port = 32151  # 端口号
# s.connect((host, port))  # 主动初始化连接
# print('---已连接---')
# info = ''
#
# while info !='Bye':
#     send_data = input("请输入要发送的数据：\n")
#     s.send(send_data.encode())  # 发送TCP数据
#     if info =='Bye':
#         break
#     info = s.recv(1024).decode()
#     print("接收的数据：",info)
# s.close()  # 关闭套接字
#

import socket
import threading
s=socket.socket()
# host=socket.gethostname()
host='192.168.120.215'
port=12345
s.connect((host,port))
print('已连接')

class read(threading.Thread):
    def run(self):
        while True:
            recvData = s.recv(2014).decode()
            print('接收到的数据为：', recvData)

class write(threading.Thread):
    def run(self):
        while True:
            send_data = input('请输入要发送的数据：')
            s.send(send_data.encode())
            if send_data == 0:
                break
        s.close()

if __name__ == '__main__':
    read = read()
    write = write()
    write.start()
    read.start()
    read.join()
    write.join()