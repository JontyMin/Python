# _*_ coding:UTf-8 _*_
# 开发团队 ：jonty
# 开发人员 ：jonty
# 开发时间 ：2020/4/16 14:51
# 文件名称 ：2、使用SQLite.py
# 开发工具 ：PyCharm

"""
SQLite不是一个客户端/服务器结构的数据库引擎 而是一种嵌入式数据库 它的数据库就是一个文件
SQLite将整个数据库 包括定义、表、索引、以及数据库本身，作为一个单独的可跨平台使用的文件存储在主机中
"""
import sqlite3

# 连接到数据库
# 数据库文件是mrsoft.db 不存在则自动创建
conn = sqlite3.connect('mrsoft.db')
# 创建一个Cursor
cursor = conn.cursor()
# 执行一条sql语句 创建user表
# cursor.execute('create table user (id int(10) primary key,name varchar(20),age int(10))')

# 添加数据
# cursor.execute('insert into user values("1","好假","22"), ("2","柳聪","22")')

# 修改数据
cursor.execute('update user set name = ? where id = ?',('昊嘉',1))

# 删除数据
cursor.execute('delete from user where id = ?'(1))
# 删除数据
# 增删改需要提交事务
# conn.commit()


# cursor.execute('select * from user ')

# cursor.execute('select * from user where id >1')

# 使用问号作为占位符 然后使用元组代替问号(注意不要忽略元组最后的逗号)
# 使用占位符的方式可以防止SQL注入
cursor.execute('select * from user where id > ?', (1,))


result = cursor.fetchall()
for i in result:
    print(i)
# 关闭游标
cursor.close()
# 关闭数据库连接
conn.close()
