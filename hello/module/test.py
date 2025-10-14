from hello.module import fibo as test

print(test.__name__)

print(test.fib(10))

print(__name__)
if __name__ == '__test__':
    print(333)

if test.__name__ == '__main__':
    print(222)
else:

    print(3333)