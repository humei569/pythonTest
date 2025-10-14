# if语句
def single_if():
    num = int(input("请输入数字："))
    if num >= 0:
        return "正数"
    else:
        return "负数"
# print(single_if())

def mul_if():
    score = int(input("请输入分数："))
    if score >= 90:
        return "优秀"
    elif score >= 80:
        return "良好"
    elif score >= 70:
        return "中等"
    elif score >= 60:
        return "及格"
    else:
        return "不及格"
# print(mul_if())

# for语句
def for_range_if():
    for i in range(1, 10):
        print(i)

    a = ['Mary', 'had', 'a', 'little', 'lamb']
    for index, item in enumerate(a):
        print(index, item)


# for_range_if()
# pass
def initlog(*agr):
    pass

# initlog("hello", "world")
# match
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return  "NotFound"
        case _:
            return "Something's wrong"

print(http_error(500))
# while语句