# _*_ coding:UTf-8 _*_
# 开发团队 ：jonty
# 开发人员 ：jonty
# 开发时间 ：2020/4/14 13:29
# 文件名称 ：string.py
# 开发工具 ：PyCharm

# 字符串综合案例
# 将字符串 "2018 Amazon Jeff Bezos 1120"进行操作
string = "2018 Amazon Jeff Bezos 1120"
print(string[5:])
print(string.replace("2018","").strip())

newlist = list(filter(str.isdigit,string))
print("".join(newlist))

string = string.replace("2018","【2018】")
string = string.replace("1120","【1120】")
print(string)

# 去除中间空格需要用到替换
string = string.replace(" ","")
print(string)


string = input("请输入一个字符串:\n")
instr = input("请输入要查找的字符:\n")
print(f"{string}中共包含{string.count(instr)}个{instr}")

instr = input("请输入字符串：\n")
newstr = list(set(instr))
newstr.sort(key=instr.index)
print(newstr)
print("".join(newstr))

