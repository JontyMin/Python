# 元组与列表相似，不同之处在于元组的元素不能修改 不可变列表
# 元组使用小括号，列表使用中括号

# 创建元组：
tup1 = ()
tup2 = ('Google', 'Twiter')
tup3 = "a", "b", "c"  # 不需要括号也可以
print(type(tup3))  # tuple

# 元组中只包含一个元素时，需在元素后面加上逗号，否则括号会被当成运算符使用
tup1 = (50)
print(type(tup1))  # 不加逗号 int

tup1 = (50,)
print(type(tup1))  # 加上逗号 tuple

# 创建数值元组 tuple()函数直接将对象创建为元组
print(tuple(range(10,20)))


# 元组可以使用下标索引来访问元组中的值
tup1 = (1, 2, 3, 4, 5)
print(tup1[1])  # 索引获取
print(tup1[:3])  # 访问前3个



# 修改元组，元组的元素值是不允许修改的，但是我们可以对元组进行组合

# 下面修改元组元素的操作是非法的'tuple' object does not support item assignment
# tup1[0] = 100
tup1 = (1, 3, 3, 4, 5) # 可以重新赋值

# 创建新元组 在进行元组连接时，连接的内容必须都是元组
# 在进行元组连接时 如果要连接的元组只有一个元素，不要忘记打逗号
tup3 = tup1 + tup2
print(tup3)

# 删除元组 元组中的元素是不允许被删除的但是可以使用del删除整个元组
del tup3
# print(tup3)  #删除之后异常信息name 'tup3' is not defined

# 元组推导式
import random
newtuple = tuple((random.randint(10,100) for i in range(10)))
print(newtuple)

# __next__() 只能是列表
number = (i for i in range(3))
print(number.__next__())
print(number.__next__())
print(number.__next__())