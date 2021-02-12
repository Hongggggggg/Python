#@sataicmethod 不能访问类变量、也不能访问实例变量
#静态方法隔断了它与类与实例之间的关系

class Student:
    role = 'Student'

    def __init__(self, name) -> None:#返回类型为None
        self.name = name
    
    @staticmethod
    def read(): #无需self，因为已经与对象无关了
        print('Reading')

s = Student('Alex')
s.read()