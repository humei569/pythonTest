# 迭代器——可以记住遍历的位置的对象
# 可以使用for循环进行遍历的都是可以迭代的对象
# 迭代器对象可以使用next函数获取下一个元素
# 迭代对象不一定是迭代器对象，但迭代器对象一定是迭代对象
# 可以使用iter函数将可迭代对象转换为迭代器对象
arr = [1, 2, 3, 4, 5]
it = iter(arr)  # 通过iter函数获取迭代器对象
print(next(it))  # 通过next函数获取下一个元素

## 自定义迭代器
class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value < self.end:
            current = self.value
            self.value += 1
            return current
        else:
            raise StopIteration
        
# my_range = MyRange(1, 5)
# print(next(my_range))
# print(next(my_range))
# print(next(my_range))


# 生成器 - 本质上是迭代器
# 本质上是一边循环一边计算出下一个元素的迭代器
# 生成器出现的原因：列表中的数据都存在内存中，数据量大时，会导致内存占用过高，
#                 生成器可以通过推导的方式计算出后续的元素，需要几个就推导出来几个，不用创建一个完整的数据列表，节省内存空间
# 生成器的创建方式：
# 1. 通过生成器表达式创建生成器
gen = (x * x for x in range(10))  # 生成器表达式
print(gen)
print(next(gen))  # 获取下一个元素
print(next(gen))
print(next(gen))

# 2. 通过生成器函数创建生成器
def my_range2(start, end):
    current = start
    while current < end:
        yield current  # yield类似于return，但会记住函数的执行状态，将指定值或者多个值返回给调用者
        current += 1

gen = my_range2(10, 15)
print(list(gen))  

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
fib = fibonacci(10)
# print(next(fib))
print(list(fib))  # 将生成器转换为列表


