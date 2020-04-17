# _*_ coding:UTf-8 _*_
# 开发团队 ：jonty
# 开发人员 ：jonty
# 开发时间 ：2020/4/14 13:53
# 文件名称 ：10、if语句.py
# 开发工具 ：PyCharm


"""
程序结构分为
顺序结构
选择结构
循环结构

选择语句 也称为条件语句
例如 如果购买的彩票号码等于公布的中奖号码 则中了大奖
if
if...else...
if...elif...else

python中没有switch语句
"""

# if语句
number = int(input("请输入你的号码:\n"))
if number == 123:  # if语句后面要加冒号 否则会报错
    print("恭喜你中奖l")

# if...else... 二选一条件  如果。。。否则。。。
# 选择Web开发/人工智能
number = int(input("请输入你的彩票号码：\n"))
if number == 123:
    print("恭喜你中奖了")
else:
    print("很遗憾没中奖")

# if...elif...else... 多分支选择
number = int(input("请输入商品销量"))
if number >= 1000:
    print("销量为A")
elif number >= 500:
    print("销量为B")
elif number >= 200:
    print("销量为C")
else:  # 只有当上面所有条件都不满足才会执行
    print("销量为D")

# elif/else 必须和if一起使用，不能单独使用

# 嵌套if
number = int(input("请输入商品销量"))
if number >= 1000:
    print("A")
else:
    if number >= 500:
        print("B")
    else:
        if number > 300:
            print("C")
        else:
            print("D")

# and 连接多条件判断
# 例如 年龄在18以上70以下可以申请小型汽车驾驶证
# 必须满足两个条件 年龄>=18  年龄<=70

age = int(input("请输入年龄：\n"))
if 18 <= age <= 70:
    print("你可以申请小型汽车驾驶")

# 使用嵌套实现
if age >= 18:
    if age <= 70:
        print("你可以申请小型汽车驾驶")

print("今有物不知其数，三三数之剩二，五五数之剩三，七七数之剩二，问几何？\n")
num = int(input("请输入你认为符合条件的数：\n"))
if num % 3 == 2 and num % 5 == 3 and num % 7 == 2:
    print("此子不凡也")
else:
    print("孺子不可教也")

# 使用or 或者 进行多条件判断 只要满足其中一个条件则执行后面的语句
sales = int(input("请输入销量"))
if sales < 10 or sales > 100:
    print("重点关注")

# 使用not 逻辑运算符 用于布尔型
data = None
if not data:
    print("You lost!")
else:
    print("You Win!")

# 在python中False,None,空字符串、空列表、空字典、空元组都相当于False
# if x is not None 是最好的写法 not x 这种写法的前提是清楚x的值
# 判断是否存在 in 不存在 not in


