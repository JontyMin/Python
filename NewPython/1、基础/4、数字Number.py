#python 数字数值类型用于存储数值
#数据类型是不允许改变的 改变值则会重新分配内存空间

#导包 取别名
import math as m
import random
from math import acos, cos, sin, tan



var1 = 1;
var2 = 10;

# 删除对象引用
del var1

# 数值类型
# 1、整形 int 
# 2、浮点型 float
# 3、复数 complex


#数字类型转换
a = 1.0;

#转换为整数
a = int(a)
print(a)

#转换为浮点型
a = float(a);
print(a)

#转换到一个复数
a = complex(a)
print(a)


#数字函数
a = -10;

# 返回绝对值
a = abs(a)
print(a)

b = 4.1;

#返回上入整数
b = m.ceil(b)
print(b)

#返回下舍整数
print(m.floor(4.9))

#返回x**y的值
print(pow(a, b))

#求平方根
print(m.sqrt(b))


#随机函数

#从0-9随机生成
a = random.choice(range(10))
print(a)


#三角函数

#返回余弦值
print(cos(12))

#返回正弦值
print(sin(12))

#返回正切值
print(tan(12))


#常量 pi 圆周率 e 自然常数
