# _*_ coding:UTf-8 _*_
# 开发团队 ：jonty
# 开发人员 ：jonty
# 开发时间 ：2020/4/13 14:10
# 文件名称 ：ASCII.py
# 开发工具 ：PyCharm

while True:
    # 用户输入字符
    c = input("请输入单个字符")
    # 判断字符长度
    if len(c) >= 2:
        # 打印提示信息
        print("字符长度超过范围，请重新输入")
    else:
        # 打印ASCII码
        print(c + "对应ASCII:", ord(c))
