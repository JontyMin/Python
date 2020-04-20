# _*_ coding:UTf-8 _*_
# 开发团队 ：jonty
# 开发人员 ：jonty
# 开发时间 ：2020/4/16 14:02
# 文件名称 ：log.py
# 开发工具 ：PyCharm

# 记录用户登录日志
import time


def show_info():
    print('''
    输入提示数字，执行相应操作
    0：退出
    1：查看登录日志
    ''')


def write_loginfo(username):
    """
    将用户名和登录时间写入日志
    :param username: 用户名
    :return:
    """
    with open('log.txt', 'a') as f:
        string = f"用户名:{username},登录时间：{time.strftime('%Y-%m-%d %H-%M-%S')}\n"
        f.write(string)


def read_loginfo():
    """
    读取日志
    :return:
    """
    with open("log.txt", 'r') as f:
        while True:
            line = f.readline()
            if line == '':
                break  # 跳出循环
            print(line)


if __name__ =='__main__':
    # 输入用户名
    username = input("请输入用户名：\n")
    # 输入密码
    password = input("请输入密码：\n")
    # 写入日志
    write_loginfo(username)
    show_info()
    num = int(input("请输入数字：\n"))
    while True:
        if num == 0:
            print("程序已退出")
            break
        elif num == 1:
            read_loginfo()
            show_info()
            num = int(input("请输入数字：\n"))

