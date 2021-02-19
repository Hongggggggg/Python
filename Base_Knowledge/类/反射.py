class Person:
    def __init__(self, name):
        self.name = name

    def read(self):
        print('%s is reading' % self.name)

p = Person('Hammer')


if hasattr(p, "name"): #查找p对象是否有name属性
    print('My name is %s' % p.name)

if hasattr(p, "name2"): #查找p对象是否有name2属性
    print('My name is %s' % p.name2)


cmd = input(">>").strip()
if hasattr(p, cmd):
    func = getattr(p, cmd)
    func()

setattr(p, "sex", "M") #设置一个静态属性
print(p.sex)

def talk(self):
    print('%s is talking' % self.name)

setattr(p, "speek", talk)#给实例添加方法
p.speek(p)#此时需将实例一并传入

setattr(Person, "talk", talk)#可以直接给类添加方法
p.talk()#此时不用传入实例

delattr(p, "sex")#删除属性
