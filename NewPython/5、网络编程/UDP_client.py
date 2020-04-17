# _*_ coding:UTf-8 _*_
# 开发团队 ：jonty
# 开发人员 ：jonty
# 开发时间 ：2020/4/17 15:32
# 文件名称 ：UDP_client.py
# 开发工具 ：PyCharm

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = input('请输入要转换的温度（单位 ：摄氏度）：\n')
s.sendto(data.encode(), ('127.0.0.1', 8080))
print(s.recv(1024).decode())
s.close()
