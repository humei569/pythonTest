# 加法
print("-----------加法运算--------------")
def add(a, b):
    return a + b
print(add(1, 2))

# 减法
print("-----------减法运算--------------")

def sub(a, b):
    return a - b

# a = input("请输入数字a：")
# b = input("请输入数字b：")
# print(sub(int(a), int(b)))
print(sub(10, 2))

# 乘法
def mul(a, b):
    return a * b
print(mul(10, 2))

# 除法
print("-----------除法运算--------------")
def div(a, b):
    return a / b
print(div(10, 2))

# 取余
print("-----------取余运算--------------")
def rem(a, b):
    return a % b

print("余数为：" , rem(10, 3))

# 向下取整
print("-----------向下取整为--------------")
def floor(a, b):
    return a // b
print(floor(10, 3))

# 乘方
print("-----------乘方运算--------------")
def pow(a, b):
    return a ** b
print(pow(10, 3))