# _*_ coding:UTf-8 _*_
# 开发团队 ：jonty
# 开发人员 ：jonty
# 开发时间 ：2020/4/14 14:59
# 文件名称 ：11、循环.py
# 开发工具 ：PyCharm


"""
反复做同一件事 成为循环
循环主要有两种：
1、重复一定次数的循环 计次循环 for循环
2、一直重复，知道条件不满足才结束 条件循环 只要条件为真 则一直循环 while循环
"""

# for循环 适用于枚举或遍历序列 迭代器对象 一般应用在循环次数已知的情况
for i in [1, 2, 3]:
    print("人生苦短，及时行乐")

for i in ["你", "是", "高", "手"]:
    print(i)

result = 0;
for i in range(101):
    result += i
print(result)

# range() 用于生成一系列连续的整数
"""
range(start,end,step)
start:指定计数的起始值 默认0
end:指定计数的结束值 包前不包后
step:指定步长 即两个数之间的间隔可以省略 步长则为1

1个参数指定的是end
2个参数指定的是start、end
"""

# 步长为2 输出所有奇数
# 1，3，5，7，9  i+2
for i in range(1, 10, 2):
    print(i, end=' ')

# 遍历字符串
string = '人生苦短'
print(string)
for c in string:
    print(c)

# while循环通过条件控制
i = 0
while i < 3:
    print("人生苦短")
    i += 1

password = 321517
i = 1
while i < 7:
    num = input("请输入密码")
    num = int(num)
    if num == password:
        print("密码正确")
        i = 7
    else:
        print(f"密码错误,已经输错{i}次了")
    i += 1
if i == 7:
    print("密码验证失败，请联系发卡行")

# 在使用while循环时 一定不要忘记添加将循环条件改变为False的代码 否则会死循环

# 允许在一个循环体嵌入另一个循环体 循环嵌套
"""
while 条件表达式1:
    while 条件表达式2:
        循环体2
    循环体1
    
for 迭代变量1 in 对象1:
    for 迭代变量2 in 对象2:
        循环体2
    循环体1

while 条件表达式:
    for 迭代变量 in 对象:
        循环体2
    循环体1

for 迭代变量 in 对象
    while 条件循环:
        循环体2
    循环体1

"""

# 当条件满足时 程序会一直执行下去 当条件满足时应该跳出循环
# 1、使用break终止循环
# 2、使用continue直接跳到下次循环

"""
break语句可以终止当前循环，包括while for在内的所有控制语句
break语句一般会结合if语句进行搭配使用 表示在某种条件下跳出循环
如果使用嵌套循环 将跳出最内层循环
"""

i = 0
while i < 3:
    print(i)
    if i == 1:  # 当i等于1的时候跳出循环
        break;
    i += 1

for item in range(10):
    if item == 5:
        break;
    print(item)


"""
continue 终止本次循环进入下次循环
一般会结合if语句使用 表示在某种条件下 跳过当前循环的剩余语句 然后进行下一轮循环
如果使用嵌套循环 将只跳过最内层循环中的剩余语句
"""

# 逢七拍腿
total= 99
for number in range(1,100):
    if number%7==0:
        continue
    else:
        string = str(num)
        if string.endswith('7'):
            continue
    total-=1
print(f"从1-99一共拍了{total}次腿")

for i in range(20):
    print((i+1)*'*')
