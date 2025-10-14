import dataclasses
from dataclasses import dataclass

if __name__ == '__classes__':
    print(666)
else:
    print(888)

print(__name__)

# print(dir())

def scope_test():
    def do_local():
        spam = "local spam"

    def do_global_test():
        global spam
        spam = "global spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal space"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:",  spam, "\n\n")

    do_global_test()
    print("After global_test_one assignment:", spam, "\n\n")

    do_nonlocal()
    print("After nonlocal assignment:", spam, "\n\n")

    do_global_test()
    print("After global_test_two assignment:", spam, "\n\n")

    do_global()
    print("After global assignment:", spam, "\n\n")


scope_test()
# global spam
# spam = 'external gobal'
print("In global scope:", spam)

class Person:
    name = '1515'
    def __init__(self, name = name):
        self.name = name
        print(self.name)
        self.data = '888'
        print(self.data)

    
    def test(self):
        self.data = 8797
        print(self.data)

person = Person(9595)
person.test()

class Man( Person ):
    def test_child(self):
        print(self.name)

# print(Man.test_child())

class Employee:
    name: str
    dept: str
    salary: int

# john = Employee('John', 'Accounting', 90000)

class Reverse:
    """对一个序列执行反向循环的迭代器。"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        print(self)
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('spam')
print(rev)
# iter(rev)
for char in rev:
    print(char)


def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('we are in the world'):
    print(char)