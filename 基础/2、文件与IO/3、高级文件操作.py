# _*_ coding:UTf-8 _*_
# 开发团队 ：jonty
# 开发人员 ：jonty
# 开发时间 ：2020/4/16 13:27
# 文件名称 ：3、高级文件操作.py
# 开发工具 ：PyCharm

"""
os提供的与文件相关的函数及说明
access()        获取对文件是否有指定的访问权限
chmod()         修改path指定文件的访问权限
remove()        删除path指定的文件路径
rename()        将文件重命名
stat()          返回文件信息
startfile()     使用相关联的程序打开指定path文件
"""

# 删除文件
import os
# os.remove(r'E:\Python\demo.txt')

# 应该先判断文件是否存在
path = r'E:\Python\demo.txt'
if os.path.exists(path):
    os.remove(path)
    print("文件删除完毕")
else:
    print("文件不存在")

#%%
# 重命名文件和目录  是文件则重命名文件 目录则重命名目录
import os
src = r'E:\Python\demo'
dst = r'E:\Python\demo1'
if os.path.exists(src):
    os.rename(src,dst)
    print("文件重命名已完成")
else:
    print("文件不存在！")

# 重命名目录时 只能修改最后一级的目录名称

# 获取文件信息
"""
stat()返回对象的常用属性
属性          说明            属性           说明
st_mode     保护模式        st_dev          设备名
st_ino      索引号          st_uid          用户ID
st_nilnk    硬连接号        st_gid          组ID
st_size     文件大小        st_time         最后访问时间
st_mtime    最后修改时间    st_ctime        最后一次状态变化时间
"""

#%%
import os
path = r'E:\Python\demo1\a.txt'
if os.path.exists(path):
    info = os.stat(path)
    print("完整路径：",os.path.abspath(path))
    print("文件大小",info.st_size)
    print("最后一次修改时间",info.st_mtime)