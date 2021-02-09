class Animal:
    type = "杂食动物"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print('I can walk')


class Person(Animal):   #继承Animal
    
    def __init__(self, name, age, sex):
        #Animal.__init__(self, name, age, sex)
        #super(Person, self).__init__(name, age, sex)#效果同上
        super().__init__(name, age)
        self.sex = sex
        print('Sex is %s' % sex)

    def speek(self):    #私有方法
        print('Speaking')



class Pig(Animal):
    type = '只吃荤的'   #重写父类属性

    def walk(self):     #重写父类方法
        #Animal.walk()   #如果只是追加在父类方法后面，可以在这里先调用一次
        super().walk()  #同上
        print('不想走')


p1 = Person('Hammer', 25, 'M')
p1.speek()
print(p1.type)

pig = Pig('pig', 2)
print(pig.type)
pig.walk()