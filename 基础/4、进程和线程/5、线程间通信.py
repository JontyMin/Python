# _*_ coding:UTf-8 _*_
# 开发团队 ：jonty
# 开发人员 ：jonty
# 开发时间 ：2020/4/17 10:26
# 文件名称 ：5、线程间通信.py
# 开发工具 ：PyCharm

# from threading import Thread
# import time
#
# def plus():
#     print('---进程1开始---')
#     global g_num
#     g_num+=50
#     print(f"g_num是{g_num}")
#     print('---进程1结束---')
#
# def minus():
#     print('---进程2开始---')
#     global g_num
#     g_num-=50
#     print(f"g_num是{g_num}")
#     print('---进程2结束---')
#
# g_num=100
#
# if __name__ == '__main__':
#     print("---主进程开始---")
#     print(f"g_num是{g_num}")
#     p1=Thread(target=plus)
#     p2=Thread(target=minus)
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     print('---主进程结束---')

# 在一个进程内所有线程共享全局变量 能够在不适用其他方式的前提下完成多线程之间的数据共享


"""
由于线程可以对全局变量随意修改 这就可能造成多线程之间对全局变量的混乱操作
一个防止他人进去的方法就是在门上加一把锁 先到的人锁上门 后到的人在门口排队 等所打开再进去
互斥锁 Mutual exclusion  缩写Mutex 防止多个线程同时读写某一块区域
互斥锁为资源引入一个状态：锁定和非锁定 当线程要更改共享数据时 先将其锁定 
此时资源的状态为锁定 其他线程不能更改 直到该线程释放资源 将资源的状态变成非锁定 其他的线程才能再次锁定该资源
互斥锁保证了每次只有一个线程进行写入操作 从而保证了多线程情况下数据的正确性
"""

# Lock类 acquire()锁定/release()释放

# from threading import Thread, Lock
# import time
#
# n = 100  # 共100张
#
#
# def task():
#     global n
#     mutex.acquire()  # 上锁
#     temp = n  # 赋值给临时变量
#     time.sleep(1)  # 休眠
#     n = temp - 1  # 数量-1
#     print(f"购买成功，剩余{n}张电影票")
#     mutex.release()  # 释放锁
#
#
# if __name__ == '__main__':
#     print('---主线程开始---')
#     mutex = Lock()  # 实例化Lock类
#     t_l = []  # 初始化列表
#     for i in range(10):
#         t = Thread(target=task)  # 实例化线程类
#         t_l.append(t)  # 放入列表
#         t.start()  # 创建线程
#     for t in t_l:
#         t.join()  # 等待线程
#     print('---主线程结束---')

# 使用互斥锁时要避免死锁 在多任务系统下 当一个或多个线程等待系统资源 而资源又被线程本身或其他线程占用 就形成了死锁


# 使用队列在线程之间通信
"""
在线程中使用queue模块的Queue队列
使用Queue在线程间通信通常应用与生产者消费者模式
产生数据的模块称为生产者
处理数据的模块称为消费者
在生产者和消费者之间的缓冲区称之为仓库
生产者负责往仓库运输商品
消费者负责从仓库取出商品
"""

from queue import Queue
import random,threading,time

# 生产者类
class Producer(threading.Thread):
    def __init__(self,name,queue):
        threading.Thread.__init__(self,name=name)
        self.data=queue
    def run(self):
        for i in range(5):
            print(f"生产者{self.getName()}将产品{i}放入仓库")
            self.data.put(i)
            time.sleep(random.random())
        print(f"生产者{self.getName()}完成")

class Consumer(threading.Thread):
    def __init__(self,name,queue):
        threading.Thread.__init__(self,name=name)
        self.data=queue
    def run(self):
        for i in range(5):
            val=self.data.get()
            print(f"消费者{self.getName()}将产品{val}从队列中取出")
            time.sleep(random.random())
        print(f"消费者{self.getName()}完成")

if __name__=='__main__':
    print('---主线程开始---')
    queue = Queue()
    producer = Producer('Producer',queue)
    consumer = Consumer('Consumer',queue)
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
    print('---主线程结束---')


# 关于线程需要注意的
"""
进程和线程的主要区别有：
1.进程是系统进行资源分配和调度的一个独立单位 线程时进程的实体 是CPU调度和分派的基本单位
2.进程之间是相互独立的，多进程中，同一个变量 各自有一份备份存在于每个进程中，但是互不影响
同一个进程的多个线程是内存共享的 所有变量都由所有线程共享
3.进程之间是独立的 因此一个进程崩溃不会影响其他进程 而线程是包含在进程之内的 线程的崩溃会引发继承的崩溃  继而导致同进程内其他线程崩溃

多线程非全局变量是否要加锁
局部变量是各自线程的 不需要加锁
"""