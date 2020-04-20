# _*_ coding:UTf-8 _*_
# 开发团队 ：jonty
# 开发人员 ：jonty
# 开发时间 ：2020/4/14 14:33
# 文件名称 ：if.py
# 开发工具 ：PyCharm


# 1、通过ASCII值判断
import sys
locki = 0;
instr = input("支付宝密码：\n")
for item in instr:
    if ord(item) > 58 or ord(item) < 47:
        locki += 1
if locki >= 1:
    print("输入的数字不合法，请重新输入！")
    instr = input("支付宝密码：\n")
    for item in instr:
        if ord(item) > 58 or ord(item) < 47:
            print("输入的数字不合法，请重新输入！")
            sys.exit()
else:
    print("支付成功")

# 2、判断输入的值是否为数字
instr = input("请输入支付密码：\n")
if instr.isdigit():
    print("支付成功")
else:
    print("支付失败，密码有误")

import random
goods = [["SanDisk U盘",149],["Micge Mouse2",550],["小米扫地机器人",1400]]
goodsel = list[random.choice[goods]]
goodprice = goodsel[1]
print(goodsel[0])
for i in range(20):
    instr = input("请输入竞猜价格:\n")
    if int(instr)>goodprice:
        print("价格高了")
    else:
        if int(instr)<goodprice:
            print("价格低了")
        else:
            print("恭喜你猜对了")
            break;