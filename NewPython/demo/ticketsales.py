# _*_ coding:UTf-8 _*_
# 开发团队 ：jonty
# 开发人员 ：jonty
# 开发时间 ：2020/4/15 16:16
# 文件名称 ：ticketsales.py
# 开发工具 ：PyCharm

import prettytable as pt


def show_tickt(row_num):
    tb = pt.PrettyTable()
    tb.field_names = ["行号", "座位1", "座位2", "座位3", "座位4", "座位5"]
    for i in range(row_num):
        l = [f"第{i + 1}行", "有票", "有票", "有票", "有票", "有票"]
        tb.add_row(l)
    print(tb)


def order_tickt(row_num):
    tb = pt.PrettyTable()
    tb.field_names = ["行号", "座位1", "座位2", "座位3", "座位4", "座位5"]
    for i in range(row_num):
        if int(row) == i + 1:
            l = [f"第{i + 1}行", "有票", "有票", "有票", "有票", "有票"]
            l[int(column)] = '已售'
            tb.add_row(l)
        else:
            l = [f"第{i + 1}行", "有票", "有票", "有票", "有票", "有票"]
            tb.add_row(l)
    print(tb)


if __name__ == "__main__":
    row_num = 13
    show_tickt(row_num)
    choose_num = input("请选择空位")
    try:
        row, column = choose_num.split(',')
    except:
        print("输入格式有误")
    order_tickt(row_num)
