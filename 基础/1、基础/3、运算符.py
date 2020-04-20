# 算数运算符
a = 21
b = 10
c = 0

c = a + b
print("+c的值是：", c)

c = a - b;
print("-c的值是：", c)

c = a * b;
print("*c的值是：", c)

c = a / b;
print("/c的值是：", c)

c = a % b;
print("%c的值是：", c)

a = 3;
b = 3;

# 幂函数
c = a ** b;
print("**c的值是：", c)

# 取整除
c = a // b;
print("//c的值是：", c)

# ----------------------------------------------------------


# 比较运算符
a = 21;
b = 10;
c = 0;

# ==
if a == b:
    print("a==b")
else:
    print("a!=b")

# !=
if a != b:
    print("a!=b")
else:
    print("a==b")

# <
if a < b:
    print("a<b")
else:
    print("a>b")

# >
if a > b:
    print("a>b")
else:
    print("a<b")

# <=
if a <= b:
    print("a<=b")
else:
    print("a>b")

# >=
if a >= b:
    print("a>=b")
else:
    print("a<b")

# ----------------------------------------------------------


# 赋值运算符

# 简单赋值
c = a + b;
print("=c:", c)

# 加法赋值
c += a;
print("+=c:", c)

# 减法赋值
c -= a;
print("-=c:", c)

# 乘法赋值
c *= a;
print("*=c:", c)

# 除法赋值
c /= a;
print("/=c:", c)

# 取模赋值
c %= a;
print("%=c:", c)

c = 3;
# 幂赋值
c **= a;
print("**=c:", c)

# 取整除赋值
c //= a;
print("//=c:", c)

# 海象运算符 可以在表达式内部为变量赋值 3.8新增
# 赋值表达式可以避免调用 len() 两次:

# if (n := len(a)) > 10:
# print(f"List is too long ({n} elements, expected <= 10


# ----------------------------------------------------------

# 逻辑运算符 and or not

a = 10;
b = 20;

if a and b:
    print("变量a和b都为true")
else:
    print("变量a和b都不为true")

if a or b:
    print("变量a和b都为true，或者其中一个为true")
else:
    print("变量a和b都不为true")

# ----------------------------------------------------------

# 成员运算符 in not in
a = 10;
b = 20;
ls = [1, 2, 3, 4, 5]

if a in ls:
    print("a在ls中")
else:
    print("a不在ls中")

if b not in ls:
    print("b不在ls中")
else:
    print("b在ls中")

# ----------------------------------------------------------

# 身份运算符 is is not
# id()函数用于获取对象内存地址
a = 20
b = 20

if a is b:
    print("a 和 b 有相同的标识")
else:
    print("1 - a 和 b 没有相同的标识")

if id(a) == id(b):
    print("a 和 b 有相同的标识")
else:
    print("a 和 b 没有相同的标识")

b = 30;
if a is not b:
    print("a 和 b 没有相同的标识")
else:
    print("a 和 b 有相同的标识")

# ----------------------------------------------------------

# 运算符优先级 与数学运算符优先级是一致的
# 先乘除后加减
# 同级运算符从左至右计算
# 可以使用()调整优先级
'''
** 最高优先级
*/%// 
+-
<= < > >=
== !=
= %= /= //= *= += -= **=
is is not
in not in
not and or

'''

a = 20
b = 10
c = 15
d = 5
e = 0

e = (a + b) * c / d  # ( 30 * 15 ) / 5
print("(a + b) * c / d 运算结果为：", e)

e = ((a + b) * c) / d  # (30 * 15 ) / 5
print("((a + b) * c) / d 运算结果为：", e)

e = (a + b) * (c / d);  # (30) * (15/5)
print("(a + b) * (c / d) 运算结果为：", e)

e = a + (b * c) / d;  # 20 + (150/5)
print("a + (b * c) / d 运算结果为：", e)
