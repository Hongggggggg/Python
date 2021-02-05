#依赖关系
class Dog:
    def __init__(self, name, master):
        self.name = name
        self.master = master
        self.introduce()

    def introduce(self):
        print("My name is %s, my master is %s" %(self.name, self.master.name))


class Master:
    def __init__(self, name):
        self.name = name
        print('My name is %s' % self.name)

master1 = Master('Hammer')
dog = Dog('金闪闪', master1)