# 拼接字符串 +号拼接字符串
mot_en = 'my name is LiuCong'
mot_cn = '记忆是一种相遇，遗忘是一种自由'
print(mot_en + mot_cn)

# 字符串不允许和其他数据类型拼接
str1 = '我今天走了'
num = 123
# 报错can only concatenate str (not "int") to str
# print(str1+num)
# 将数字转换成字符串
print(str1 + str(num))

# 计算字符串的长度
str1 = '人生苦短，我用Python'
length = len(str1)  # 计算字符串长度
print(length)

# 默认情况下len()计算字符串长度是不区分英文、数字、汉字 ，所有字符都是1个
# 实际开发需要获取字节数 可以通过encode()编码后在进行获取
length = len(str1.encode())  # utf-8编码
print(length)

length = len(str1.encode('gbk'))  # GBK编码
print(length)

# 字符串截取
# 字符串也属于序列 截取字符串可通过切片方法实现
# 字符的索引跟序列的索引是一样的
substr1 = str1[1]  # 截取第2个字符
substr2 = str1[5:]  # 从第6个字符开始截取
substr3 = str1[:5]  # 从左边开始截取5个字符串
substr4 = str1[2:5]  # 截取第3个到第5个字符
print('原字符串：', str1)
print(substr1 + '\n' + substr2 + '\n' + substr3 + '\n' + substr4)

# 截取字符串时 如果指定索引不存在 会报异常 异常处理
try:
    substr5 = str1[15]
except IndexError:
    print('指定索引不存在')

# 字符串分割
# str.split(sep,maxsplit)
# sep指定分割字符
# maxsplit可选参数 指定分割次数
# 如果不指定sep参数那么也不能指定maxsplit参数
# 如果不指定参数，则默认采用空白符分割，不论有几个空白符都作为一个空白符进行分割
str1 = '人 生 苦 短 >>> 我 用 P . y . t . h . o . n'
print('原字符串：', str1)
list1 = str1.split()  # 默认分割符
list2 = str1.split('>>>')  # 采用多个字符分割
list3 = str1.split('.')  # 采用'.'进行分割
list4 = str1.split(' ', 4)  # 采用空格进行分割，并且只分割前4个
print(str(list1) + '\n' + str(list2) + '\n' + str(list3) + '\n' + str(list4))

# 检索字符串
# count() 用于检索指定字符串在另一个字符串中出现的次数，不存在则返回0
str1 = '@小米 @华为 @魅族'
print(f'字符串“{str1}”中包括{str1.count("@")}个@符号')

# find()用于检索是否包含指定的子字符串 存在则返回出现的索引 否则返回-1
# rfind()从右边开始查找
print(f'字符串“{str1}”中@符号首次出现的位置索引为：{str1.find("@")}')

# 如果只是想判断指定字符串是否存在 in
print('@' in str1)

# index()检索是否包含指定字符串 类似find() 使用index()，当指定字符串不存在时会抛出异常
print(f'字符串“{str1}”中@符号首次出现的位置索引为：{str1.index("@")}')

# startswith() 检索字符串是否以指定子字符串开头
print(f'判断字符串“{str1}”是否以@符号开头，结果为：{str1.startswith("@")}')
# endswith() 检索字符串是否以指定子字符串结尾
print(f'判断字符串“{str1}”是否以@符号结尾，结果为：{str1.endswith("@")}')

# 大小写转换
# lower() 转小写
str1 = 'Python'
print(str.lower(str1))

# upper()转大写
print(str.upper(str1))

# 去除字符串中的空格和特殊字符 '\t','\n','\r',
# strip() 去掉字符串左右两侧的空格和特殊符
str1 = ' https://www.microsoft.com \t\r\n'
print(str1.strip())

# 指定要移除的字符 可指定多个字符
str2 = '@微软科技.@.'
print(str2.strip('@.'))

# lstrip()去除左侧空格和特殊符
# rstrip()去除右侧空格和特殊符


# 格式化字符串
# 先制定一个模板 预留空位，根据需要填上相应的内容
# ‘%’操作符
print("我叫 %s 今年 %d 岁!" % ('python', 10))

# 使用字符串对象的format方法
str1 = '编号：{:0>9}\t公司名称： {:s} \t官网： https://www.{:s}.com'  # 定义模板
txt1 = str1.format('7', '百度', 'baidu')  # 转换内容
print(txt1)
