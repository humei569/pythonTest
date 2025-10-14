import functools
import time


class CountCalls:
    def __init__(self, func):
        # functools.update_wrapper(self, func)
        self.func = func
        print("func:", self.func)
        self.count = 0
        print('count：', self.count)

    # __call__()是python类的一个特殊方法，是类实现装饰器、仿函数的关键机制
    #
    def __call__(self, *args, **kwargs):
        self.count += 1
        print("已经被调用：", self.count, "次")
        print("param:", *args, **kwargs)
        return self.func(*args, **kwargs)


    def timer(func):
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            end = time.perf_counter()
            print("运行时间：", end - start)
            return result
        return wrapper