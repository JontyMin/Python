# _*_ coding:UTf-8 _*_
# 开发团队 ：jonty
# 开发人员 ：jonty
# 开发时间 ：2020/4/15 13:33
# 文件名称 ：13、类和对象.py
# 开发工具 ：PyCharm

"""
类是面向对象编程的核心 面向对象程序设计是在面向过程程序设计的基础上发展而来的
它比面向过程编程具有更强的灵活性和扩展性

面向对象 Object Oriented 简写OO 设计思想
面向对象编程 Object Oriented Programming 即OOP

"""

"""
对象 抽象概念 表示任意存在的事物 万物皆对象 对象是事物存在的实体
将对象分为两部分：
1、静态部分 属性 如性别
2、动态部分 行为 如进食


类 封装对象的属性和行为的载体 具有相同属性和行为的一类实体称为类 如人类


OOP的特点
封装
封装是面向对象编程的核心思想 将对象的属性和行为封装起来 其载体就是类
类通常会对用户隐藏实现细节
采用封装思想保证了类内部数据结构的完整性
使用该类的用户不能直接看到类中的数据结构
而只能执行类允许公开的数据，避免外部对内部数据的影响 提高程序的可维护性


继承
继承是实现重复利用的重要手段 字类通过继承父类的属性和行为的同时又添加了字类特有的属性和行为

多态
将父类对象应用于字类的特征就是多态
"""


# 定义类 class
class Person:
    """
    人类
    """
    pass
    # ...


# 创建实例 python中不使用new关键字
newper = Person()
print(newper)


# 创建类之后 会自动创建一个__init__()方法 类似于构造方法
# 每创建一次类的新实例 都会自动执行
# 该方法必须包含一个self参数 而且必须是第一个参数
# self参数是一个指向实例本身的引用 用于访问类中的属性和方法
# %%
class Geese:
    """大雁类"""

    def __init__(self):  # 构造方法
        print("我是大雁类")


wildGeese = Geese()


# %%
class Haojia:
    """好假"""
    age = 12
    height = 1.78
    weight = 80
    sex = '男'

    # def __init__(self,height,weight,sex):
    #     print("我是好假类，我有一下特征：")
    #     print(height)
    #     print(weight)
    #     print(sex)
    def __init__(self):
        print("大家好我是好假类")
        print(f"我今年{Haojia.age}岁,身高{Haojia.height},体重{Haojia.weight},我是{'公' if Haojia.sex == '男' else '母'}的")

    def hello(self):  # 创建实例方法 self必要参数
        print("大家好我是刘昊嘉")


# height = 1.8
# weight = 80
# sex = '男'
hj = Haojia()
hj.hello()  # 类的实例名.方法名


# 访问限制
# 单下划线 protected 受保护的 只允许类本身和子类访问
# 双下划线 private 私有的 只允许类本身访问 不能通过类的实例访问
# 首尾双下划线 定义特殊方法 系统定义的名字 __init__()
# %%
class Swan:
    '''天鹅类'''
    _neck_swan = '天鹅脖子很长'  # 定义私有属性

    def __init__(self):
        print("__init__():", Swan._neck_swan)


swan = Swan()
print('直接访问：', swan._neck_swan)


# %%
class Swan:
    '''天鹅类'''
    __neck_swan = '天鹅脖子很长'  # 定义私有属性

    def __init__(self):
        print("__init__():", Swan.__neck_swan)


swan = Swan()
# print('直接访问：',swan.__neck_swan)  # 不能通过实例名访问
print('类名访问', swan._Swan__neck_swan)  # 通过实例名.类名__xxx访问


# %%
# python中 通过@property装饰器将一个方法转换为属性
class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height


rect = Rect(20, 40)
print(rect.area)


# %%
# 如果想要限制属性不能在类体外修改 可以设置为私有的 但设置为私有的后 在类体外也不能获取它的值
# 如果想创建一个可读取不可修改的属性 可使用@property
class TVshow:
    def __init__(self, show):
        self.__show = show

    @property
    def show(self):
        return self.__show


tvshow = TVshow('红海行动')
print('修改前', tvshow.show)

tvshow.show = '战狼2'
print('修改后', tvshow.show)

# 在python中 可以在类定义语句中 类名右侧使用一对小括号将要继承的基类括起来
"""
class ClassName(baseclass):
    '''类文档'''
    statement  类体
"""


# %%
# 方法重写 当基类中的某个方法不完全适用于派生类时则需要重写该方法
class Fruit:
    color = '绿色'
    def __init__(self,color):
        Fruit.color=color
    def harvest(self, color):
        print(f'水果是：{color}的')


class Orange(Fruit):
    color = '橙色'

    def __init__(self):
        print('我是橙子')

    def harvest(self):
        print(f'橙子是{Orange.color}的')


orange = Orange()
orange.harvest()


# 派生类调用基类__init__()
class Apple(Fruit):
    def __init__(self):
        print('我是苹果')
apple = Apple()
apple.harvest('绿色')