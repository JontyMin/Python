# _*_ coding:UTf-8 _*_
# 开发团队 ：jonty
# 开发人员 ：jonty
# 开发时间 ：2020/4/17 15:47
# 文件名称 ：15、异常处理及程序调试.py
# 开发工具 ：PyCharm

"""
python常见异常
NameError           尝试访问一个没有声明的变量引发的错误
indexError          索引超出序列范围引发的错误
IndentationError    缩进错误
ValueError          传入的值错误
KeyError            请求一个不存在的字典关键字引发的错误
IOError             输入输出错误
ImportError         当import语句无法找到模块或from无法在模块中找到相应的名称时引发
AttributeError      尝试访问未知的对象属性引发的错误
TypeError           类型不合适引发的错误
MemoryError         内存不足
ZeroDivisionErroe   除数为0引发的错误

"""


# try...except...语句
# 把可能产生异常的代码放在try语句中，把处理结果放在except语句块中
# 在使用try...except语句捕获异常时 如果except后面不指定异常名称则表示捕获全部异常
# 捕获异常后 当程序出错 输出错误信息 程序会继续执行

def division():
    num1 = int(input("请输入被除数：\n"))
    num2 = int(input("请输入除数：\n"))
    result = num1/num2
    print(result)

# if __name__ == '__main__':
#     try:
#         division()
#     except ZeroDivisionError as z:
#         print(z)
#         print("除数不能为0")


# try...except...else...
if __name__ == '__main__':
    try:
        division()
    except ZeroDivisionError as z:
        print(z)
    else:
        print("程序执行完成")
    finally:
        print("我进来了")
# try...except..finally
# 无论是否引发异常finally子句都可以执行


# 使用raise语句抛出异常
# 如果某个函数或方法可能会产生异常 但不想在当前函数或方法处理这个异常
# 可以使用raise语句在函数或方法中抛出异常
def division():
    num1 = int(input("请输入被除数：\n"))
    num2 = int(input("请输入除数：\n"))
    if num2 ==0:
        raise ValueError("除数不能为0")
    result = num1/num2
    print(result)