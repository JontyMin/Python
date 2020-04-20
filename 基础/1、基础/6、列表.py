# 序列是python中的基本数据结构
# 列表的数据项不需要具有相同的数据类型

list1 = ['Google', 'Apple', 2001, 2002]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c"]

# 列表的索引从0开始，列表可以进行截取、组合

print("list1[0]:", list1[0])
print("list2[1:5]", list2[1:5])

# 更新列表
# 可以对列表数据项进行修改或更新 也可使用append()方法添加项
print("第三个元素是：", list1[2])
list1[2] = 1998
print("更新后第三个元素是：", list1[2])

# 删除列表元素 del remove
print("原始列表：", list1)
del list1[2]
print("删除第三个元素", list1)

# 列表对+和*的操作与字符串类似，+用于组合列表，*用于重复列表

# 列表长度
print(len(list1))

# 组合
list4 = list2 + [1, 2, 3]

# 重复
list5 = ['hi'] * 3

# 元素是否存在于列表中
print(3 in list2)

# 迭代(遍历)
for item in list4:
    print(item)

for item in list5:
    print(item)

# 列表截取和拼接
l = ['Google', 'Micrsoft', 'FaceBook']

# 读取第三个元素
print(l[2])

# 从右侧开始读取
print(l[-2])

# 输出从第几个元素开始之后的所有元素
print(l[1:])

# 拼接
l += ['Apple', 'HuaWei']
l.append('hah')
for item in l:
    print(item)

# 嵌套列表
a = ['a', 'b', 'c']
b = [1, 2, 3]
x = [a, b]
for item in x:
    print(item)

# 得到得到第一组第2个
print(x[0][1])

# 列表函数
# len()列表长度
print(f"二维数组的长度：{len(x)}")

# 返回列表最大值
print(max(b))
# 返回列表最小值
print(min(b))

# 将元组转换为列表
# list(seq)

# 列表方法

# 在列表末尾添加新的对象
b.append(4)

# 统计某个元素在列表中出现的次数
b.count(1)

# 在列表末尾追加另一个序列的多个值
b.extend([2, 3, 4])

# 在列表中找出某个值第一个匹配项的索引值
b.index(1)

print()
# 将对象插入列表
b.insert(2, [9, 0, 9])

# 移除列表中的一个元素(默认最后一个元素)，并且返回该值
b.pop()

# 移除列表中某个值的第一个匹配项
del b[1]

# 删除不确定位置的元素使用remove
# 但是如果指定的元素不存在则会报错
# 所以使用remove之前先判断该元素是否存在
b.remove(1)
for item in b:
    print(item)
print()

team = ["火箭", "勇士", "开拓者"]
val = "火箭"
if team.count(val) > 0:  # 判断该元素是否存在
    team.remove(val)

# 反向列表中的元素
b.reverse()
for item in b:
    print(item)

a = [1, 4, 3, 2]

# 列表排序
a.sort()
for item in a:
    print(item)

# reverse可选参数 True降序 False升序 默认升序
a.sort(reverse=True)
for item in a:
    print(item)

char = ['cat', 'Tom', 'Angela', 'pet']
char.sort()  # 默认区分大小写
char.sort(key=str.lower)  # 不区分大小写

# 采用sort()对中文支持不好，排序的结果与我们常用的音序排序法或者笔画排序法不一致
# 如果需要实现对中文内容列表排序，需要重新编写相应的方法进行处理

# 使用sorted() 用于对列表进行排序，使用该函数进行排序后，原列表元素顺序不变
grade = [12, 32, 43, 54, 64, 54, 87]
print(grade)
grade_as = sorted(grade)
print(grade_as)
grade_desc = sorted(grade, reverse=True)  # 降序
print(grade_desc)
# 列表清空
a.clear()

# 复制列表
b = a.copy()

# 将序列组合为一个索引序列
team = ["法国", "比利时", "阿根廷"]
for index, item in enumerate(team):
    print(index + 1, item)

# 统计列表元素和
grade = [65, 34, 64, 75, 34, 23]
total = sum(grade)

# 列表推导式
# 使用列表推导式可以快速生成一个列表 或者根据某个列表生成满足指定需求的列表
import random

rdnumber = [random.randint(10, 100) for i in range(10)]
print(rdnumber)

# 例 定义一个商品价格列表，应用列表推导式生成一个将全部商品价格打五折的列表
price = [1200, 2300, 4300, 3200]
sale = [int(x * 0.5) for x in price]
print(sale)

# 条件筛选
sale = [x for x in price if x > 10]
print(sale)
