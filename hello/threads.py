# 多任务/多线程 —— 同时运行多个任务（线程）
# 进程：操作系统分配资源的基本单位，每一个进程至少有一个线程 
#      一个进程默认有一个主线程, 也可以创建多个子线程，没有进程就没有线程
# 线程：CPU的基本调度单位，每一个进程至少有一个线程，这个线程称为主线程

# Python的多线程是通过threading模块实现的
# 1. 导入threading（线程）模块
import threading
import time

class ThreadTask(object):
    def task_one(self):
        print("Task one is running")
        time.sleep(2)
        print("Task one is done")

    def task_two(self):
        print("Task two is running")
        time.sleep(2)
        print("Task two is done")

thread = ThreadTask()
# 2. 创建线程对象
t1 = threading.Thread(target=thread.task_one)  # 创建线程对象
t2 = threading.Thread(target=thread.task_two)  # 创建线程对象

# print(t1)
# print(t1.name)  # 线程名称
# 4. 守护线程
t1.daemon = True # 设置为守护线程，主线程结束后，守护线程也会结束
t2.daemon = True # 设置为守护线程，主线程结束后，守护线程也会结束

# 3. 启动线程
t1.start()  # 启动线程
t2.start()  # 启动线程

# 5. 主线程等待子线程结束
t1.join()  # 主线程等待t1线程结束
t2.join()  # 主线程等待t2线程结束


print("Main thread is running")

# 
