# _*_ coding:UTf-8 _*_
# 开发团队 ：jonty
# 开发人员 ：jonty
# 开发时间 ：2020/4/14 10:29
# 文件名称 ：9、正则表达式.py
# 开发工具 ：PyCharm

# 处理字符串时经常会有查找某些复杂规则的字符串需求 字符串就是用来描述这些规则的工具

# 行定位符 用来描述子串的边界 '^'表示行的开始 '$'表示行的结尾
str1 = '^tm'
# 元字符
"""
. 匹配除换行符之外的任意字符
\w 匹配字母、数字、下划线或汉字
\W 匹配除字母、数字、下划线或汉字之外的字符
\s 匹配单个空白符 tab 换行符
\S 除单个空白符之外的字符
\d 匹配数字
\b 匹配单词的开始或结束，单词的分界符通常是空格、标点符号或者换行
"""

# 限定符 匹配特定数量的字符
str1 = '^\d{8}$' # 此表达式可匹配8位数字

"""
常用限定符
? 匹配前面的字符0/1次 colou?r 可匹配colou/color
+ 匹配前面的字符多次 go+gle 可以匹配gogle-goo...gle
* 匹配前面的字符0-多次 go*gle 可以匹配ggle-goo...gle
{n} 匹配前面的字符n次  go{2}gle 只匹配google
{n,} 匹配前面的字符至少n次， go{2,}gle 可以匹配gogle-goo...gle
{n,m} 匹配前面的字符最少n次，最多m次 employee(0,2) 可匹配employ,employe,employee
"""

# 字符类 匹配没有预定义的元字符 需要在方括号里列出来
# [aeiou] 匹配元音字母
# [.?!] 匹配.、?、！标点符号

#排除字符
# [^a-zA-Z] 排除字符

# 选择字符 包含条件选择的逻辑 需要选择字符 | (或者)
# (^\d{15$})|(^\d{18}$)|(^\d{17})(\d|X|x)$  # 匹配身份证好

# 转义字符  \ 将特殊字符转成普通字符
# [1-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}

# 分组 () 子表达式
# (\.[0-9]{0,3}){3} 对分组进行重复操作

# 在python中使用正则表达式
import re

# match() 用于从字符串开始处匹配 如果在开始位置匹配成功 则返回match对象，否则none
# 当第一个字母不符合条件时 不再进行匹配
pattern = r'mr_\w+'  # 模式字符串
string = 'MR_Shop mr_shop'
match = re.match(pattern,string,re.I) # 不区分大小写
print(match)
print(match.start())  # 起始位置
print(match.end())  # 结束位置
print(match.span())  # 匹配位置的元组
print(match.string)  # 要匹配的字符串
print(match.group())  #匹配数据


# search() 用于在整个字符串中搜索第一个匹配的值 匹配成功则返回match对象 否则none
# search() 方法不仅在字符串的起始位置搜索，其他位置有符合的匹配也可以
match = re.search(pattern,string,re.I)
print(match)



# findall() 用于在整个字符串中搜索所有符合正则表达式的字符串，并以列表的形式返回
match = re.findall(pattern,string,re.I)
print(match)

#%%
import re
pattern = r'([1-9]{1,3}(\.[0-9]{1,3}){3})'
str1 = '127.0.0.1 192.168.1.66'
match = re.findall(pattern,str1)
print(match)
for item in match:
    print(item[0])
#%%
# sub() 字符串替换
pattern = r'1[3-9]\d{9}'
string = '中奖号码为：321517，联系电话为：18173608896'
result = re.sub(pattern,'1xxxxxxxxxx',string)
print(result)

# split() 分割字符串
pattern = r'[?|&]'
url = 'https://www.microsoft.com/account?user="jonty"&pwd="mic"'
result=re.split(pattern,url)
print(result)