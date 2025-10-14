## 单例模式和魔术方法
# 单例模式
#   使用场景：
#       1. 回收站对象
#       2. 日志对象
#       3. 数据库连接对象
#       4. 线程池对象
#       5. 配置文件对象
#       6.音乐播放器对象，一个音乐播放器软件负责播放一个音乐对象
#       7.游戏中的场景管理器
#   确保某一个类中只有一个实例存在
#   优点：可以节省内存空间
#   缺点：不能实现多线程(多线程访问时容易引发线程安全问题)
#   实现方式：
#   1. 通过@classmethod
#   2. 通过装饰器
#   3. 重写__new__方法
class SigletonWithNew(object):
    """通过重写__new__方法实现单例模式"""
    _instantce = None
    # 每个类在执行实例化时，都会调用__new__方法，且先调用__new__方法，再调用__init__方法
    # 每实例化一次，都会调用__new__方法，且返回一个实例对象，分配一个内存地址
    # 单例模式，每次实例化时，都返回同一个实例对象，内存地址相同
    def __new__(cls, *args, **kwargs):
        if cls._instantce == None:
            print("cls.isinstance is None")
            cls._instantce = super().__new__(cls)
            print("new被调用")

        print("cls.isinstance is not None")
        return cls._instantce


    def __init__(self):
        print("init被调用")

    


# singleton = SigletonWithNew()
# print(singleton)
# singleton2 = SigletonWithNew()
# print(singleton2)


    
#   4. 导入模块
from hello.packTest.SigletonWithModule import SigletonWithModule as singleton
from hello.packTest.SigletonWithModule import SigletonWithModule as singleton1

print('模块导入', id(singleton))
print('模块导入2', id(singleton1))


## 魔术方法
print(SigletonWithNew.__doc__) ## 获取多行注释的内容
print(singleton.__module__)
print(singleton.__class__)
