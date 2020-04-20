# _*_ coding:UTf-8 _*_
# 开发团队 ：jonty
# 开发人员 ：jonty
# 开发时间 ：2020/4/17 9:03
# 文件名称 ：2、进程池.py
# 开发工具 ：PyCharm

# 如果要创建很多的进程 则使用multiprocessing提供的Pool类 即Pool进程池
"""
Pool常用方法
apply_async(func[])     使用非堵塞方式调用func()函数(并行执行，堵塞方式必须等待上一个进程推出才能执行下一个进程)
apply(func[])           使用堵塞方式调用线程
close()                 关闭线程池 使其不再接受新的任务
terminate()             不管任务是否完成 立即终止
join()                  主程序堵塞 等待子程序退出 必须在close或terminate之后使用

"""

from multiprocessing import Pool
import os,time

def task(name):
    print(f"子进程{os.getpid()}执行task{name}...")
    time.sleep(1)   # 休眠1秒

if __name__=='__main__':
    print(f"父进程{os.getpid()}")
    p=Pool(3)       # 进程池最大进程数3
    for i in range(10):
        p.apply_async(task,args=(i,)) # 使用堵塞方式调用task()函数
    print("等待所有子进程结束...")
    p.close()       # 关闭进程池 不接受新请求
    p.join()        # 等待子进程结束
    print('所有进程结束')