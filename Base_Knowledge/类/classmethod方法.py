class Dog:
    def __init__(self, name):
        self.name = name

    @classmethod
    def run(cls): #当被classmethod修饰时，第一个默认参数不再是对象本身，而是类本身
        print(cls)
        print(Dog)
        '''
        使用classmethod修饰后, cls.name相当于Dog.name,而Dog类并没有定义name这个属性，所以这里会报错
        '''
        #print('%s is running' % cls.name) 


d = Dog('旺财')
d.run()