# window —— cmd python
# python 标识符由字母、数字、下划线组成
# 不能以数字开头，区分大小写
# 标识符中不能包含空格 特殊符号

"""
python中以下划线开头的标识符有特殊意义，一般避免使用相似的标识符
1、以单下划线开头的标识符 _width 表示不能直接访问的类属性 也不能导入
2、以双下划线开头的标识符 __add 表示类的私有成员
3、以双下划线开头或结尾的是Python专用标识 __init__()表示构造函数
"""

# 同一行可多条语句

# 输出
print("hello python")

# 输入
name = input('请输入姓名：')
print(name)

# Python 的代码块不使用大括号 {} 来控制类，函数以及其他逻辑判断。
# python 最具特色的就是用缩进来写模块。
if 1 > 0:
    print("OK")
else:
    print("No")

print("nono")  # 没有严格缩进会报错 IndentationError:

# 多行语句
# Python语句中一般以新行作为语句的结束符。

# \将一行语句分为多行
# total = item_one + \
#     item_two + \
#         item_three

# 语句包含[],{},()不需要使用\
days = ["Mondy", "Tuesday",
        "Wednesday"]

for item in days:
    print(item)

# 引号
# 可使用引号'、双引号"、三引号'''或""" 表示字符串
word = 'word'
sentence = "这是一个句子"
paragraph = """这是一个段落。
包含多行多语句"""

print(paragraph),
print(word),
# 注释
# 单行注释 #
# 多行注释 """  '''

"""
这是多行注释
"""

# print 默认输出是换行的，如果要实现不换行需要在变量末尾加上逗号 ,。
x = "a"
y = "b"
# 换行输出
print(x)
print(y)

print('---------')
# 不换行输出  无效
print(x),
print(y),

# 不换行输出
print(x, y)

# 缩进相同的一组语句构成一个代码块，我们称之代码组。
# 像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。
# 首行及后面的代码组称为一个子句(clause)

if True:
    print(1)
else:
    print(1)

# 命令函参数 输入Python -h

# 内置函数type()可以返回变量类型
a = 11
print(type(a))

# id()返回变量所指的内存地址
b = 11
print(id(a))
print(id(b))

print(r'adfadfad\"jaja')