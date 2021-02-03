class Dog:
    d_type = '二哈' #公共属性

    def __init__(self, name, age): #初始化方法，构造函数，实例化时会自动执行，进行一些初始化工作
        print('hello', name, age)
        self.name = name #绑定参数到对象self中
        self.age = age

    def play(self): #第一个参数必须是self，代表对象本身,如果没有self,就不知道是哪个对象调用的函数
        print("i am playing....", self)


dog1 = Dog('哮天犬', 3)
dog2 = Dog('二郎神', 4)

dog1.play() #相当于dog1.play(dog1), self就代表dog1
print(dog1) #打印dog1与self值会发现是相等的


class People:
    nationality = 'CN'#公共属性

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

p1 = People('JQK', 20, 'M')
p2 = People('123', 24, 'F')

print(p1.nationality, p2.nationality, People.nationality)#公共属性是一致的
p2.nationality = 'JP' #相当于p2创建了一个新的实例属性，原公共属性nationality不受影响
print(p1.nationality, p2.nationality, People.nationality)



