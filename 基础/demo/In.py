# _*_ coding:UTf-8 _*_
# 开发团队 ：jonty
# 开发人员 ：jonty
# 开发时间 ：2020/4/13 14:37
# 文件名称 ：In.py
# 开发工具 ：PyCharm

# 用户输入要转换的数字
number = input("请输入数字：")
# 输入当前进制类型
type = input("请输入要转换的进制类型：")
num = int(number, int(type))
print(number+f"的{type}进制为：", num)

str = input("请输入底数：")
num = input("请输入幂:")
print(str+f"的{num}次幂为",int(str)**int(num))

