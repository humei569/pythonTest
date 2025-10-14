class Person:
    def __init__(self):
        self.name = '张三'
        self.age = 18
        print(self.name, self.age)

    def __str__(self):
        return "Person: %s, %d" % (self.name, self.age)

    def eat(self):
        print("吃吃吃")

    def sing(self):
        print("唱歌")