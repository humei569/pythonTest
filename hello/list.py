list_data = [6, 'dd', 'dkhd', 4, 4447, 'ddkjoww', 425]

print(list[0])

list_data.append('商品')
print(list)

list_data.insert(0, 'first')
print(list_data)

list_data.remove(4)
print(list_data)

list_data.pop(1)
print(list_data)

print(list_data.index(4447, 0, 4))

print(list_data.count(425))
# sorted(list_data)
# print(list_data)

# list_data.sort()
# print(list_data)

list_data.reverse()
print(list_data)

list_data_copy = list_data.copy()
list_data_copy.append('list_data_copy')

print(list_data_copy, list_data)

list_data.clear()
print(list_data)

from collections import deque
queue = deque([], maxlen=3)
queue.append([11,22, 33, 44])
print(queue)


queue = deque(["Eric", "John", "Michael"])
print(queue)
queue.index("Eric")
queue.count()

squares = list(map(lambda x: x**2, range(10)))
print(squares)


test = lambda a : a + 10
print(test(3))


squares = [x**2 for x in range(10)]
print(squares)

a = set('abracadabra')
print(a)

# sorted(a)
print(a)

b = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(b)

