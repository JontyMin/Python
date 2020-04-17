# _*_ coding:UTf-8 _*_
# 开发团队 ：jonty
# 开发人员 ：jonty
# 开发时间 ：2020/4/16 14:29
# 文件名称 ：1、数据库编程接口.py
# 开发工具 ：PyCharm


"""
数据库连接对象 Connection Onject 主要提供数据库游标对象和提交回滚事务的方法 以及如何关闭数据库连接

connect()函数常用参数
dsn             数据源名称
user            用户名
password        密码
host            主机
database        数据库
"""

import pymysql

# 1、获取连接对象
conn = pymysql.connect(host='127.0.0.1',
                       user='root',
                       password='root',
                       database='db_stu',
                       charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor)
conn.close()

# 2、连接对象的方法
"""
close()     关闭连接
commit()    提交事务
rollback()  回滚事务
cursor()    获取游标，操作数据库
"""

# 游标对象
"""
Cursor Onject 代表数据库中的游标 用于指示抓取数据操作上下文
主要提供执行sql语句 调用存储过程 湖区查询结果

游标对象方法说明

callproc()      调用存储过程
close()         关闭当前游标
execute()       执行数据库操作 sql语句或数据库命令
executemany()   用于批量操作
fetchone()      获取查询结果集中的下一条记录 
fetchmany()     获取指定数量的记录
fetchall()      获取结果集的所有记录
nextest()       跳至下一个可用结果集
arraysize()     指定使用fetchmany()获取的行数 默认1
setinputsizes() 设置在调用execute*()方法时分配的内存区域大小
setouputsizes() 设置列缓冲区大小
"""