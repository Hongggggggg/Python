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