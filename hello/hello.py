#coding=utf-8
print("Hello python")

# a,b = 100, 300
# print(a+b)
# print(a,b)

# x = input("请输入一个数字：")
# print("这个数字是" + x)
#
# num = int(x) # 类型转换

# fp = open("text.txt", "w")
# print("人生苦短", file=fp)
# fp.close()

# x = 10
# y = 7
#
# x //= y
#
# print(x)
#
#
# c,d = 30,60
# c,d = d,c
# print(c,d)

# num = int(input("请输入一个数字："))
# num1 = num % 10
# num2 = num % 100 // 10
# num3 = num // 100 % 10
# num4 = num // 1000
#
# print(num1, num2, num3, num4)

# a = 10
# if a < 10:
#     print("a小于10")
# elif a > 10:
#     print("a大于10")
# else:
#     print("a等于10")
#
# if not a:
#     print("a为空")
# else:
#     print("a不为空")
#
# b= False
# if a & b:
#     print("a和b都为真")
# else:
#     print("a和b有一个为假")

# a = 10
# for i in "10":
#     print(i)
#
# sum = 0
# for i in range(1,11):
#     print(i)
#     sum += i
#
# print(sum)

def solution(cards):
    # Edit your code here
    result = {}
    for i in cards:
        index = cards[i]
        if cards[i] not in result:
            result[index] = 1
        else:
            result[index] += 1

    print( result)
    # print(result[1])

    return 0

print(solution([1, 1, 2, 2, 3, 3, 4, 5, 5]))