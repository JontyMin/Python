# _*_ coding:UTf-8 _*_
# 开发团队 ：jonty
# 开发人员 ：jonty
# 开发时间 ：2020/4/16 9:04
# 文件名称 ：1、基本文件操作.py
# 开发工具 ：PyCharm


"""
在变量和序列中存储的数据是暂时的 程序结束后会丢失
为了能长时间保存程序中的数据 需要将程序中的数据保存到磁盘文件中
python中提供了内置的文件对象和对文件、目录操作的模块
"""

# 在使用文件对象时首先需要通过内置的open()方法创建文件文件对象
# 然后通过该对象提供的方法进行文件的基本操作

# 1、创建和打开文件

# 当文件不存在时 会抛异常：
# 1.在当前目录下创建一个要打开的文件
# 2.在调用open时，指定mode的参数值为w、w+、a、a+ 当文件不存在时自动创建新文件
file = open('demo.txt', 'a+')

# 2、以2进制形式打开文件
file = open('picture.png', 'rb')
print(file)

# 3、打开文件指定编码格式
file=open('demo.txt','r',encoding='utf-8')


# 关闭文件 打开文件后要及时关闭 以免对文件造成不必要的措施
file.close()  # 关闭文件对象


# 打开时使用with
# 打开文件后要及时关闭 另外如果抛出了异常将导致文件不能及时关闭
# 为了避免此类问题 python提供了with语句 在文件处理时 无论是否抛出异常
# 都能保证在with语句执行完之后关闭已经打开的文件
#%%
with open('demo.txt','w') as file:  # 创建或打开保存应用信息文件
    print(file)

#%%
# 写入文件内容
with open('demo.txt','a') as file:
    file.write(input("请输入内容：\n"))
# 在调用write方法向文件中写入内容的前提是 打开文件时 指定的打开模式是w(可写)/a(追加) 否则会报错


#%%
# 读取文件 指定读取字符
with open('demo.txt','r+') as file:
    string=file.read(4)
    print(string)
# 在调用read读取文件内容的前提是 打开文件模式是r(只读)/r+(读写)

#%%

# read()方法是从文件头开始读取的，如果想要读取部分内容 可以使用seek()将文件的指针移动到新的位置 在进行读取
with open('demo.txt','r') as file:
    file.seek(4)  # 指定值是按一个汉字占两个或三个字符(GBK占两个，UTF-8占3个) 英文和数字各占一个
    string=file.read(4)
    print(string)

#%%
# 读取一行 readline()
with open('demo.txt','r') as file:
    number = 0;
    while True:
        number+=1
        line = file.readline()
        if line=='':
            break
        print(number,line,end='\n')

#%%
# 读取全部行 readlines()返回字符串列表
with open('demo.txt','r') as file:
    message = file.readlines()
    # print(message)
    for item in message:
        print(item)