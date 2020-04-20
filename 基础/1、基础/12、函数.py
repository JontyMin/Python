# _*_ coding:UTf-8 _*_
# 开发团队 ：jonty
# 开发人员 ：jonty
# 开发时间 ：2020/4/15 10:21
# 文件名称 ：12、函数.py
# 开发工具 ：PyCharm


"""
在python中函数的应用非常广泛 例如用于输出的print()
输入的input(),生成整数的range()...这都是内置的标准函数
python支持自定义函数 将一段有规律、重复的代码定义为函数，达到一次编写多次调用的目的
使用函数可以提高代码重复利用率
"""


def fun_bmi(person, height, wieght):  # 形式参数
    """
    根据身高体重计算BMI指数
    :param person: 姓名
    :param height: 身高，单位：米
    :param wieght: 体重，单位：千克
    :return: none
    """
    print(person + "的身高:" + str(height) + "米\t体重：" + str(wieght) + "千克")


# 调用函数
fun_bmi("好假", 1.70, 60)  # 实际参数


def fun_none():
    pass  # 什么也不做的函数 pass占位符
    ...


fun_none()


# %%
# 定义函数
def demo(obj):
    print("原值:", obj)
    obj += obj


# 调用函数
print("=====值传递=====")
mot = "唯有在被追赶的时候，你才能真正地奔跑"
print("函数调用前：", mot)
demo(mot)  # 采用不可变对象字符串
print("函数调用后：", mot)

print("=====引用传递=====")
list1 = ['邓肯', '奥尼尔', '帕克']
print("函数调用前：", list1)
demo(list1)  # 采用可变对象 列表
print("函数调用后：", list1)

# 位置参数也成为必备参数 必须按照正确位置传递到函数中 即调用时的数量和位置必须和定义时一致
# 由于调用函数时，传递的实参位置与形参位置不一致时，并不会抛出异常，在调用函数时一定要确定好位置

# 关键字参数 使用形参的名字来确定传入的参数值，不再需要与形参的位置完全一致，只需要将参数名写正确即可
demo(obj='hah')

# 给参数设置默认值
# 在定义参数时直接指定形参默认值
# 指定默认形参必须在所有参数最后
# 在python中可以使用函数名.__default__ 查看函数的默认值参数
demo.__defaults__


# %%
def demo1(obj=None):  # 使用None作为可变参数的默认值
    if obj == None:
        obj = []
    print(obj)
    obj.append(1)


demo1([1])
demo1()


# 定义函数时 为形参设置默认值要牢记：默认参数必须指向不可变对象

# 可变参数 不定长参数
# *par/**par

# %%
# *par 接收任意多个实际参数将其放到一个元组
def printplayer(*name):
    print("\n我最喜欢的明星有：")
    for item in name:
        print(item)


printplayer('李沁', 'ts')


#%%
# **par 接收多个显式赋值的实际参数 将其放入字典中
def printsign(**sign):
    print()
    for key, value in sign.items():
        print('[' + key + ']的绰号是：' + value)


printsign(邓肯='石佛', 上将='罗宾逊')

#%%
# 返回值
def getUser(name):
    user = 'bich'
    return user+name

username = getUser('好假')
print(username)

# 当函数中没有return语句时 或者省略掉了return语句参数时，将返回None

#%%
# 变量作用域
# 局部变量/全局变量
# 当局部变量和全局变量重名时，对函数体的变量进行赋值后 不影响函数体外的变量
# 函数体内的变量加上global后也可以作为全局变量
# 实际开发不建议全局变量和局部变量同名
message = '唯有在被追赶的时候，你才能真正地奔跑'
print('函数体外：',message)
def f_demo():
    global message
    message='命运给予我们的不是失望之酒，而是机会之杯'
    print('函数体内：',message)

f_demo()
print('函数体外：',message)

# 匿名函数 没有名字的函数 这样的函数只是用一次
# 在python中使用lambda表达式创建匿名函数
# 使用lambda表达式时 参数可以有多个 用，分隔 表达式只能有一个，只能返回一个值 且不能出现其他非表达式语句
# lambda表达式首要用途是指定短小的回调函数
#%%
import math
r =10
result = lambda r:math.pi*r*r
print(result(r))

"""
python常用内置函数
dict()      创建一个字典
help()      用于查看函数或模块用途的详细说明
dir()       收集参数信息
hex()       十进制转十六进制
next()      返回迭代器下一个项目
divmod()    把除数和榆树运算结果结合起来返回一个包含商和余数的元组
id()        获取对象的内存地址
sorted()    对所有可迭代的对象进行排序
ascii()     返回一个表示对象的字符串
oct()       将一个整数转换成八进制字符串
bin()       返回一个整数或长整数的二进制形式
open()      用于打开一个文件
str()       将对象转化为适于人阅读的形式
sum()       对序列进行求和计算
filter()    用于过滤序列
format()    格式化字符串
"""