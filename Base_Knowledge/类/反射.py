import sys
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

if __name__ == '__main__': #__name__如果是在模块本身获取，则为“__main__”,如果是在其他模块导入，则为"反射.py"
    print('module self call') #只有在当前模块本身运行程序才会打印这句话

mod = sys.modules[__name__]
print(mod.p)
if hasattr(mod, 'p'): 
    o = getattr(mod, 'p')
    print(o)

#其他模块也可以直接使用

'''

if hasattr(反射, 'p'): 
    o = getattr(mod, 'p')
    print(o)
'''
