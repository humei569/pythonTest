import functools


def login():
    print("login system")

def sendMsg():
    print("send message")

def main(fn):
    fn()

main(login)

# 装饰器
# 本质是闭包函数
    # 闭包的条件  1. 嵌套函数  2. 闭包函数内部引用外部函数的变量 3. 外部函数返回内部函数
def decorators(func):
    def wrapper():
        func()
    return wrapper

dec = decorators(sendMsg)
dec()

# 装饰器语法糖
def decorators_new(fn):
    def wrapper(x):
        fn(x)
    return  wrapper

@decorators_new
def sendMsg2(x):
    print(x)
    print("send 2 message")
sendMsg2(222)
#
# @decorators_new
# def sendNewData():
#     print("send new data")
# sendNewData()
# dec_new = decorators_new()


print("----------------------------")

def repeat(n):
    def decorators(func):
        # @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorators

@repeat(3)
def say(msg):
    print(msg)

say("hi")
