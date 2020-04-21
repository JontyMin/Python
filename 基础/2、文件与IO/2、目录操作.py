# _*_ coding:UTf-8 _*_
# 开发团队 ：jonty
# 开发人员 ：jonty
# 开发时间 ：2020/4/16 10:43
# 文件名称 ：2、目录操作.py
# 开发工具 ：PyCharm

"""
目录也称文件夹 用于分层保存文件 通过目录可以分门别类的保存文件
也可以通过目录快速找到想要的文件 python中操作目录需要使用内置os/os.path模块
os模块是python内置的与操作系统功能和文件系统相关的模块 该模块中的语句在不同的操作系统中运行可能会有不同的结果
"""

# os/os.path模块
import os

name = os.name  # 用于获取操作系统类型 nt>windows  posix>Linux、Unix、MaxOS
print(name)

print(os.linesep)  # 换行符 \r\n

print(os.sep)  # \\路径分隔符

print(os.getcwd())  # 获取当前工作目录

print(os.listdir('E:/Python/基础'))  # 返回指定目录下文件和目录信息

"""
os提供
madir(path)             创建新目录
makedirs(path1,path2)   创建多级目录
rmdir(path)             删除目录
removedirs(path1,path2) 删除多级目录
chdir(path)             把path设置为当前工作目录
walk()                  遍历目录树 返回一个元组 包括所有路径名、目录列表 文件列表


os.path提供
abspath(path)           用于获取文件或目录的绝对路径
exists(path)            判断目录或文件是否存在
join(path,name)         将目录与目录或者文件名连接起来
splitext()              分离文件名和扩展名
basename(name)          从一个目录中提取文件名
dirname(path)           从一个路径中提取文件路径，不包括文件名
isdir(path)             判断是否为路径
"""

#%%
# 路径 用于定位一个文件或目录的字符串
# 1.相对路径
# 2.绝对路径

# 当前工作目录是指当前文件所在的目录 相对路径是依赖于当前工作目录的
import os
print(os.getcwd())  # 获取当前工作目录
# 获取工作目录下子文件夹中的文件
with open("文件与IO/demo.txt") as file:  # 通过相对路径打开文件
    print(file.read())

# 指定文件路径时需要对文件路径分隔符'\'进行转义 即将'\'替换成'\\' 也可以将'\'用'/'代替
# 在路径字符串之前加上r 就不不要进行转义了
with open(r"文件与IO\demo.txt") as file:  # 通过相对路径打开文件
    print(file.read())

#%%
# 绝对路径 在使用文件时指定文件的实际路径 不依赖于当前工作路径
import os
print(os.path.abspath(r"文件与IO\demo.txt"))  # 获取绝对路径

# 拼接路径 将多个路径拼接在一起 使用os.path.join()
print(os.path.join(r"E:\Python\NewPython",r"文件与IO\demo.txt"))
# 如果在要拼接的路径中没有一个绝对路径 那么最后拼接出来的将是绝对路径
# 使用路径拼接并不会检测该路径是否真实存在
# 把两个路径进行拼接时，不要使用字符串拼接 而是使用os.path.join()函数 这样可以正确处理不同操作系统的路径分隔符

#%%
# 判断目录是否存在
import os
print(os.path.exists('c://demo1'))
print(os.path.exists("c://demo.txt"))  # 判断文件是否存在

#%%
# 创建目录
# 1、创建一级目录 一次只能创建一级目录
import os
# os.mkdir(r"E:\Python\demo")

# 这个时候如果再次创建目录会报错
# FileExistsError 文件已存在
path = r"E:\Python\demo"
if not os.path.exists(path):
    os.mkdir(path)
    print("目录已创建")
else:
    print("目录已存在")

# 2、创建多级目录
os.makedirs(r"E:\Python\demo\dir\mr\hj")


#%%
# 删除目录
import os
os.rmdir(r"E:\Python\demo\dir\mr\hj")

# 如果要删除的目录不存在会抛异常
path = r"E:\Python\demo\dir\mr\hj"
if os.path.exists(path):
    os.rmdir(path)
    print("目录删除成功")
else:
    print("该目录不存在")

# os.rmdir(path) 只能删除空目录
# 删除非空目录
import shutil
shutil.rmtree(path)  # 删除该目录下的所有子目录和内容


#%%
# 遍历目录
import os
tuples = os.walk(r"/基础\基础")
for i in tuples:
    print(i,'\n')