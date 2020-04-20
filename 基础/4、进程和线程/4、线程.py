# _*_ coding:UTf-8 _*_
# 开发团队 ：jonty
# 开发人员 ：jonty
# 开发时间 ：2020/4/17 10:03
# 文件名称 ：4、线程.py
# 开发工具 ：PyCharm

# 线程时操作系统能够进行运算调度的最小单位
# 它被包含在进程之中 是进程中的实际运作单位
# 一条线程指的是进程中一个单一顺序的控制流
# 一个进程中可以并发多个线程 每个线程并行执行不同的任务

# 使用threading模块创建线程
# Thread参数：
# target表示一个可调用对象 线程启动时 run()方法调用此对象
# name 表示当前线程名 默认创建一个Thread-N格式唯一名称
# args 表示传递给target()函数的参数元组
# kwargs 表示传递给target()函数的参数字典

# import threading, time
#
#
# def process():
#     for i in range(3):
#         print(f"thread name is {threading.current_thread().name}")
#
#
# if __name__ == '__main__':
#     print('--主线程开始---')
#     threads = [threading.Thread(target=process) for i in range(4)]  # 创建4个线程
#     for t in threads:
#         t.start()
#     for t in threads:
#         t.join()
#     print('---主线程结束---')

# 线程执行的顺序时不确定的

# 使用Thread子类创建线程
import threading, time


class SubThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "子线程" + self.name + '执行，i=' + str(i)
            print(msg)


if __name__ == '__main__':
    print('--主线程开始---')
    t1 = SubThread()
    t2 = SubThread()
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print('---主线程结束---')
