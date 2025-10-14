class Object:
    def __init__(self, *args, **kwargs):
        print(args)
        print(kwargs)
        for key, value in args:
            print(key, value)
            # setattr(self, key, value)
        print("构造函数")

    def __del__(self):
        print("析构函数")

    __age = 18 ## 隐藏属性，一般是python中的魔法属性/方法，轻易不要定义
    def get_hide_attribute(self):
        return self.__age

    # 私有属性  外部可以使用，跨文件不可用
    _name = "张三"
    def get_private_attribute(self):
        return self._name


# object = Object({"name": "张三", "age": 18})
object = Object()
print(object)

# 获取隐藏属性
print(object.get_hide_attribute())

# 获取私有属性
print(object.get_private_attribute())
print(object._name)