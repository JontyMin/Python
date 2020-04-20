# _*_ coding:UTf-8 _*_
# 开发团队 ：jonty
# 开发人员 ：jonty
# 开发时间 ：2020/4/17 9:18
# 文件名称 ：3、队列.py
# 开发工具 ：PyCharm

# 每个进程都有自己的地址空间、内存、数据栈以及其他记录其运行状态的辅助数据
#%%
# from multiprocessing import Process
# def plus():
#     print('---进程1开始---')
#     global g_num
#     g_num+=50
#     print(f"g_num是{g_num}")
#     print('---进程1结束---')
# def minus():
#     print('---进程2开始---')
#     global g_num
#     g_num-=50
#     print(f"g_num是{g_num}")
#     print('---进程2结束---')
#
# g_num=100
# if __name__ == '__main__':
#     print("---主进程开始---")
#     print(f"g_num是{g_num}")
#     p1=Process(target=plus)
#     p2=Process(target=minus)
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     print('---主进程结束---')
#%%


"""
两个g_num都是初始值都是100
全局变量没有在进程中传递 即进程间没有共享信息
进程间的通信 multiprocessing 包装了底层的机制
提供了Queue(队列)、Pipes(管道)等多种方式交换数据

多进程队列使用
Queue方法：
Queue.qsize()       返回当前队列包含的消息数量
Queue.empty()       判断队列是否为空
Queue.full()        判断队列是否已满
Queue.get()         获取队列中的一条消息，然后移除
Queue.get_nowait()  相当于get()
Queue.put()         将消息写入队列
Queue.put_nowait    相当于put
"""

# 使用队列
# from multiprocessing import Queue
#
# if __name__ == '__main__':
#     q = Queue(3)    # 初始化一个que对象，最多可接受三条put消息
#     q.put("消息1")
#     q.put("消息2")
#     print(q.full()) # 判断队列是否已满 False
#     q.put("消息3")
#     print(q.full()) # True
#
#     try:
#         q.put("消息4",True,2)
#     except:
#         print(f"消息队列已满，当前消息数{q.qsize()}")
#
#     try:
#         q.put_nowait("消息4",True,2)
#     except:
#         print(f"消息队列已满，当前消息数{q.qsize()}")
#
#
#     # 读取消息时 先判断消息队列是否为空 再读取
#     if not q.empty():
#         print('---从队列中读取消息---')
#         for i in range(q.qsize()):
#             print(q.get_nowait())
#
#     # 先判断消息队列是否已满 再写入
#     if not q.full():
#         q.put_nowait("消息4")

# 使用队列在进程中通信
from multiprocessing import Process,Queue
import time

# 向队列中写入数据
def write_task(q):
    if not q.full():
        for i in range(5):
            message = "消息"+str(i)
            q.put(message)
            print(f"写入：{message}")

# 从队列读取数据
def read_task(q):
    time.sleep(1)
    while not q.empty():
        print(f"读取：{q.get(True,2)}")  # 等待2秒

if __name__ == "__main__":
    print('---父进程开始---')
    q=Queue()
    pw = Process(target=write_task(q))
    pr = Process(target=read_task(q))
    pw.start()
    pr.start()
    pw.join()
    pr.join()
    print('---父进程结束---')
