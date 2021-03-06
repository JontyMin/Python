# _*_ coding:UTf-8 _*_
# 开发团队 ：jonty
# 开发人员 ：jonty
# 开发时间 ：2020/4/17 13:10
# 文件名称 ：1、网络基础.py
# 开发工具 ：PyCharm

"""
互联网协议簇 即通用协议标准

TCP/IP 简介

IP协议
在通信是，通信双方必须知道对方的标识
互联网上每个计算机的唯一标识就是IP地址
IP地址实际上就是一个32位整数(称为IPv4)
它是以字符串表示的IP地址
IP协议负责把数据从一台计算机通过网络发送到另一台计算机
数据被分割成小块，然后通过IP包发送出去
由于互联网链路复杂 两条计算机之间经常有多条线路
因此路由器就负责决定如何把一个IP包发送出去
IP包特点就是按块发送 途径多个路由 但不保证都能到达 也不保证顺序到达

TCP协议则是建立在IP协议之上的 TCP协议负责在两台计算机之间建立可靠连接
保证数据包按顺序到达 TCP协议会通过3次握手建立可靠连接
然后需要对每个IP包进行编号，确保对方按顺序收到，如果包掉了则自动重发


一个TCP报文除了包含要传输的数据，还包含源IP地址和目标IP地址、源端口和目标端口

端口：
在两台计算机通信时 只发送IP地址是不够的 因为同一台计算机运行着多个网络程序
一个TCP报文来了之后到底交给哪个程序 就需要端口来区分 每个网络程序都想操作系统申请唯一的端口号

一个进程也可能同时与多个计算机链接 因此他会申请很多端口 端口号不是随意使用的 而是按照一定的规则进行分配的


UDP 面向无连接的协议
使用UDP协议不需要建立连接 只需要知道对方的IP地址和端口号 就可以直接发送数据包
但是无法保证数据数据到达 使用UDP传输数据不可靠 但是优点是比TCP协议的速度快


Socket简介
为了让两个程序通过网络进行通讯 二者必须使用Socket套接字
套接字是用于描述IP地址和端口 它是一个通信链的句柄 可以实现不同计算机或虚拟机之间的通信
在主机上一帮运行了多个服务软件 同时提供几种服务 每种服务都打开一个Socket 并绑定到一个端口上
不同的端口对应不同的服务
"""
import socket
# s = socket.socket(AddressFamily,Type)
# AddressFamily 可以选择AF_INET(用于internet进程间通信)或者AF_UNIX(用于同一台机器进程间的通信)
tcpSock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# Type 套接字类型 可以是SOCK_STREAM(流式套接字，主要用于TCP协议)或者SOCK_DDGRAM(数据报套接字 主要用于UDP协议)
tcpSock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


"""
socket对象方法：
bind()            绑定地址(host,port)到套接字 以元组的形式表示地址
listen()          开始TCP监听 
accept()          被动接受TCP客户端连接(阻塞式) 等待连接的到来
connect()         主动初始化TCP服务器连接
recv()            接收TCP数据，数据以字符串形式返回
send()            发送TCP数据 
sendall()         完整发送TCP数据
recvfrom()        接收UDP数据
sendto()          发送UDP数据
close()           关闭套接字
"""