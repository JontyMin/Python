# _*_ coding:UTf-8 _*_
# 开发团队 ：jonty
# 开发人员 ：jonty
# 开发时间 ：2020/4/16 16:11
# 文件名称 ：1、进程.py
# 开发工具 ：PyCharm


# 多任务 顾名思义是指操作系统能够执行多个任务
"""
进程是计算机中已运行程序的实体，进程与程序不同 程序本身只是指令、数据及其组织形式的描述
进程才是程序的真正运行实例

"""

# 使用multiprocessing模块创建进程
from multiprocessing import Process  # 导入模块

# def test(interval):
#     print("我是子进程")
#
# def main():
#     print("主进程开始")
#     p=Process(target=test,args=(1,))  # 实例化
#     p.start()  # 启动子进程
#     print("主进程结束")
#

# if __name__ == "__main__":
#     main()

"""
is_alive()      判断进程是否还在执行
join()          是否等待进程实例执行结束 或等待多少秒
start()         启动进程实例 创建子进程
run()           如果没有给定target参数 对这个对象调用start()方法时 将执行对象中的run()方法
terminate()     不管任务是否完成 立即终止

属性
name 当前进程实例别名
pid  当前进程实例的pid值
"""

#%%
from multiprocessing import Process
import time
import os

# 两个子进程将会调用的方法
def child_1(interval):
    print(f"子进程{os.getpid()}开始执行，父进程为{os.getppid()}")
    t_start=time.time()  # 计时开始
    time.sleep(interval)  # 程序被挂起的时间
    t_end = time.time()  # 计时结束
    print(f"子进程{os.getpid()}执行时间为{t_end-t_start}秒")

def child_2(interval):
    print(f"子进程{os.getpid()}开始执行，父进程为{os.getppid()}")
    t_start=time.time()  # 计时开始
    time.sleep(interval)  # 程序被挂起的时间
    t_end = time.time()  # 计时结束
    print(f"子进程{os.getpid()}执行时间为{t_end-t_start}秒")

if __name__=='__main__':
    print("---父进程开始执行---")
    print(f"父进程PID：{os.getpid()}")  # 输出当前程序的PID
    p1 = Process(target=child_1,args=(1,))  # 实例化进程p1
    p2 = Process(target=child_2,name='mi', args=(2,))  # 实例化进程p2
    p1.start() # 启动进程p1
    p2.start() # 启动进程p2
    # 同时父进程往下执行 如果p2还在执行 返回True
    print(f"p1.is_alive={p1.is_alive()}")
    print(f"p2.is_alive={p2.is_alive()}")
    # 输出p1和p2进程的别名和PID
    print(f"p1.name={p1.name}")
    print(f"p1.PID={p1.pid}")

    print(f"p2.name={p2.name}")
    print(f"p2.PID={p2.pid}")

    print("---等待子进程---")
    p1.join()
    p2.join()
    print("---父进程执行结束---")


#%%
# 使用Process子类创建进程 要处理复杂任务的进程
# 通常定义成一个类 使其继承自Process类 每次实例化这个类的时候 就等同于实例化一个进程对象
from multiprocessing import Process
import time
import os

# 继承Process
class SubProcess(Process):
    '''由于Process类本身也有__init__()方法 这个子类相当于重写了父类这个方法'''
    def __init__(self,interval,name=''):
        Process.__init__(self)  # 调用父类初始化方法
        self.interval = interval  # 接收参数interval
        if name:                  # 判断传递的参数name是否存在
            self.name=name        # 如果传递参数name 则为子进程创建name属性

    # 重写run()方法
    def run(self):
        print(f"子进程{os.getpid()}开始执行,父进程为{os.getppid()}")
        t_start = time.time()  # 计时开始
        time.sleep(self.interval)  # 程序被挂起的时间
        t_stop = time.time()  # 计时结束
        print(f"子进程{os.getpid()}执行时间为{t_stop - t_start}秒")

if __name__ == '__main__':
    print("---父进程开始执行---")
    print(f"父进程PID：{os.getpid()}")  # 输出当前程序的PID
    p1 = SubProcess(interval=1,name='haojia')  # 实例化进程p1
    p2 = SubProcess(interval=2)  # 实例化进程p2
    p1.start()  # 启动进程p1
    p2.start()  # 启动进程p2
    # 同时父进程往下执行 如果p2还在执行 返回True
    print(f"p1.is_alive={p1.is_alive()}")
    print(f"p2.is_alive={p2.is_alive()}")
    # 输出p1和p2进程的别名和PID
    print(f"p1.name={p1.name}")
    print(f"p1.PID={p1.pid}")
    print(f"p2.name={p2.name}")
    print(f"p2.PID={p2.pid}")
    print("---等待子进程---")
    p1.join()
    p2.join()
    print("---父进程执行结束---")