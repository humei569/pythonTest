class SigletonWithModule:
    def __init__(self):
        print(self)
        print("模块单例被调用")

singleton = SigletonWithModule()