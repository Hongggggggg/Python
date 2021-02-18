class Student:
    def __init__(self, name):
        self.name = name

    @property #将方法变为属性
    def reading(self):
        print('%s is reading' % self.name)


s1 = Student('Hammer')
s1.reading #调用属性的时候不需要加括号


class Flight:
    def __init__(self, num):
         self.num = num

    def check_status(self):
        print('check the plane %s' % self.num)
        return 1

    @property #get
    def flight_status(self):
        status = self.check_status()
        if status:
            print('%s has arrived' % self.num)

    @flight_status.setter #set
    def flight_status(self, status):
        print('change status to %d' % status)

    @flight_status.deleter #del
    def flight_status(self):
        print('Del')


f = Flight('H80688')
f.flight_status
f.flight_status = 10
del f.flight_status


