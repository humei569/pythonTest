from hello.packTest import test1, decoratorsCountCalls, Object

test1.login()

@decoratorsCountCalls.CountCalls
def foo(x):
    return x * 2
foo(2)
print(foo(5))

@decoratorsCountCalls.CountCalls.timer
def bar(x):
    return x * 3

print(bar(5))

object = Object.object

print(object.get_hide_attribute())

# object = Object

# print(object.get_private_attribute())
# print(Object._name)


