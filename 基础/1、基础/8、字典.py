# _*_ coding:UTf-8 _*_
# 开发团队 ：jonty
# 开发人员 ：jonty
# 开发时间 ：2020/4/13 10:46
# 文件名称 ：8、字典.py
# 开发工具 ：PyCharm

"""
字典和列表类似，也是可变序列 不过是无序的 保存的内容是以键值对的形式
特征：
1、通过键而不是索引获取
2、字典是任意对象的无序集合
3、字典是可变的 可任意嵌套
4、字典中的键必须唯一
5、字典中的键必须不可变
"""

dic = {'key1': '刘昊嘉', 'key2': '柳聪'}
print(dic)

# 映射函数创建字典
rid = [1, 2, 3]
name = ['刘昊嘉', '柳聪', 'jonty']
dic = dict(zip(rid, name))
print(dic)

# 给定关键字参数
dic = dict(邓肯='石佛', 帕克='跑车')
print(dic)

# 使用fromkeys()方法
namelist = ['邓肯', '哈佛逊', '帕克']
dic = dict.fromkeys(namelist)
print(dic)

# 通过元组和列表创建
name_tuple = ('邓肯', '哈佛逊', '帕克')
sign = ['石佛', '妖刀', '跑车']
dic = {name_tuple: sign}
print(dic)

# 通过键值对访问字典
# print(dic['石佛'])
dic = {'key1': '刘昊嘉', 'key2': '柳聪'}
# 当指定键值不存在时 返回一个默认值
print(dic.get('key1', '查无此人'))

# 遍历字典
for item in dic.items():
    print(item)

for key, value in dic.items():
    print(key + " " + value)

'''
还提供了values() keys() 用于返回字典的值和键列表
'''

# %%
# 添加修改删除字典元素
dic = dict((('邓肯', '石佛'), ('集落比利', '妖刀'), ('帕克', '跑车')))
dic['罗宾逊'] = '海军上将'  # 添加一个元素 键不存在则添加
print(dic)
dic['帕克'] = '迈凯伦'  # 修改一个元素 键存在则修改
print(dic)
del dic['帕克']  # 删除一个元素 但是如果键不存在 报异常
print(dic)
if '帕克' in dic:  # 如果存在则删除
    del dic['帕克']
print(dic)
# %%

# 字典推导式
import random

randic = {i: random.randint(10, 100) for i in range(1, 5)}
print(randic)
# 删除字典 del
# del dic
# 清空字典全部元素
# dic.clear()

"""
python 中的集合和数学中的集合类似
也是用于保存不重复元素的
集合最好的应用是去重复 集合中的每个元素都是唯一的
集合是无序的 可能每次输出的元素排列顺序与上次不一样
"""
# %%
# 集合的创建
set1 = {'好假', '柳聪', '奥里给'}
print(set1)

set2 = set('命运给予我们的不是失望之酒，而是命运之杯')

# 在创建空集合时 只能通过set()函数实现 而不能使用{} 直接使用{}表示创建空字典
# 集合的添加和删除
set1.add('jonty')
print(set1)

if '柳聪' in set1:
    set1.remove('柳聪')  # 指定移除元素 不存在则会抛异常
print(set1)
set1.pop()  # 移除一个元素
set1.clear()  # 清空集合

# %%
# 集合最常用的操作就是进行交集、并集、差集运算
pf = set(['邓肯', '加内特', '马龙'])
print('前锋位置有', pf)
cf = set(['邓肯', '奥尼尔', '姚明'])
print('中锋位置有', cf)

# 即使前锋又是中锋
print('交集运算', pf & cf)

# 前锋和中锋
print('并集运算',pf | cf)

# 是前锋但不是中锋
print('差集运算',pf - cf)

"""
列表、元组、字典、集合的差异
数据结构    是否可变    是否重复    是否有序    定义符号
列表         是         是          是         []
元组         否         是          是         ()
字典         是         是          否     {key:value}
集合         是         否          否         {}
"""