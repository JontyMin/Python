# _*_ coding:UTf-8 _*_
# 开发团队 ：jonty
# 开发人员 ：jonty
# 开发时间 ：2020/4/17 15:24
# 文件名称 ：3、UDP编程.py
# 开发工具 ：PyCharm

# UDP是面向消息的协议 UDP一般用于多点通信和实时的数据业务
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 创建UDP套接字
s.bind(('127.0.0.1', 8080))  # 绑定地址到套接字
print('绑定UDP到8080端口')
data, addr = s.recvfrom(1024)  # 接收数据
data = float(data) * 1.8 + 32  # 转化公式
send_data = '转换后的温度（单位：华氏摄氏度）：' + str(data)
print('Recrived from ', addr)
s.sendto(send_data.encode(), addr)  # 发送给客户端
s.close()
