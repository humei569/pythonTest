# 继承
from hello.packTest.Person import Person


class Female(Person):
    def sing(self):
        print("---------------------")
        print("female is singing, but not good")

    def dance(self):
        print("---------------------")
        print("female is dancing")

# female = Female()
# female.sing()
# print(female)


class Children(Female):
    def sing(self):
        # super(),继承父级的方法
        print("---------------------")
        parent = super()
        parent.sing()
        print("children is singing")
    pass

children = Children()
print(children.sing())
print(children.dance())

class Test(object):
    def __init__(self):
        self.name = "张三"
        self.age = 18
        print(self.name, self.age)

    def __str__(self):
        return "Person: %s, %d" % (self.name, self.age)

    def eat(self):
        print("吃吃吃")

    def sing(self):
        print("唱歌")


#----------------------------------------------------------------------------------------------------------------------
## 静态方法
# 静态方法没有self、cls参数的限制
# 静态方法和类无关，静态方法可以访问类属性，静态方法不可以访问实例属性
# 一般在工具类中使用
class TestStatic(object):
    @staticmethod
    def static_method():
        print("静态方法")

    @staticmethod
    def static_method_with_param(param):
        print(f"带有{param}参数的静态方法")

static = TestStatic()
static.static_method()
static.static_method_with_param("name") # 静态方法只有在调用，取消不必要的参数传递，有利于减少不必要的内存占用和性能消耗

# ----------------------------------------------------------------------------------------------------------------------
## 类方法
class ClassStatic(object):
    @classmethod
    #cls代表类本身
    def class_method(cls):
        print(cls)
        print("类方法")

    @classmethod
    def class_method_with_param(cls, param):
        print(f"带有{param}参数的类方法")

ClassStatic.class_method()
ClassStatic.class_method_with_param("name")