class Brand: 
    def __init__(self, name):
        self.name = name
    
    def __getitem__(self, item):
        return self.__dict__[item]

    def __setitem__(self, key, value):
        print('set item')
        self.__dict__[key] = value

    def __delitem__(self, key):
        print('del...')

    def __delattr__(self, item):
        print('Del...')

    def __str__(self):
        return 'Str %s' % self.name

    def __repr__(self):
        return 'Repr %s' % self.name

    def __del__(self): #当对象被释放（主动del，程序结束被动释放）时会调用此函数
        print('对象被释放')



b = Brand('Hammer')#将属性变为字典
print(b['name'])

b['web'] = 'www.hammer.com'#添加key，value
print('===', b.web, b['web'])

print(str(b), repr(b))
print(b)

'''
str函数或者print调用时，执行的是obj.__str__()
repr函数或者解释器中调用时，执行的是obj.__repr__()
如果未定义__str__方法，则使用__repr__()来代替
'''

#用new方法实现单例模式
class Printer:
    tasks = []
    instance = None #存放第一个实例对象
    def __init__(self, name):
        self.name = name

    def add_task(self, job):
        self.tasks.append(job)
        print('[%s] 添加任务[%s]到打印机，总任务数[%s]' % (self.name, job, len(self.tasks)))

    #__new__方法是用来执行__init__方法的
    def __new__(cls, *arg, **kwargs):
        #只有第一次实例化的时候正常进行，后面每次实例化，并不创建新的实例
        if cls.instance is None:
            obj = object.__new__(cls)
            print("obj", obj)
            cls.instance = obj
        return cls.instance #以后每次实例化都直接返回第一次存的实例对象

p1 = Printer('Word')
p2 = Printer('PDF')

p1.add_task('word')
p2.add_task('pdf')

print(p1, p2)
