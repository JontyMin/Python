# _*_ coding:UTf-8 _*_
# 开发团队 ：jonty
# 开发人员 ：jonty
# 开发时间 ：2020/4/16 15:22
# 文件名称 ：3、使用MySQL.py
# 开发工具 ：PyCharm

import pymysql


# 打开数据库连接 可以额外设置字符集'charset=utf-8' 防止插入中文报错
db = pymysql.connect('127.0.0.1','root','root','db_stu')

# 使用cursor()创建一个游标对象
cursor = db.cursor()

# 使用excute方法执行sql

# 批量添加
data = [("李老师","男"),("张老师","男"),("刘老师","男"),("王老师","男"),]

cursor.executemany('insert into user (name,sex) values(%s,%s)',data)

db.commit()

cursor.execute('select * from user')

for i in cursor.fetchall():
    print(i)

db.close()



