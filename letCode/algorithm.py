import cmath
import math


# x的平方根
def sqrt(x):
    # Python 自带的sqrt函数
    root = math.sqrt(x)
    print(root)
    print(int(root))

    # 二分法：
    index = 0
    left = 0
    right = x
    while(left < right):
        mid = int(left + (right - left) / 2)
        # mid = left + (right - left) / 2
        if(math.pow(mid, 2) <= x):
            index = mid
            left = mid + 1
        else:
            right = mid - 1

    print(index)
    return index

    # 牛顿迭代


sqrt(999)