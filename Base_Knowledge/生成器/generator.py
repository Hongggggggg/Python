#创建
g = (x * x for x in range(10))#将列表生成器左右的中括号变成小括号

print(g)

#取值
print(next(g))

#遍历
for i in g:
    print(i, end = ' ') #第一个0已经被取走了


#函数生成器,斐波那契数列
def fib(n):
    a, b = 0, 1
    count = 0
    while count < n:
        temp = a
        a = b
        b = temp + b
        yield b #暂停 return
        count += 1

g = fib(20)
print(g.__next__())
print(next(g))
print("=======")
print(next(g))#会继续从上一次yield的地方继续执行

print(fib(20))

for i in fib(20):
    print(i)


def g_test():
    while True:
        n = yield
        print("receive from outside: ", n)

g = g_test()
g.__next__() #send之前必须调用一次生成器，此时会发送None至yield

for i in range(10):
    g.send(i)#发送i

#单线程下的多并发
def consumer(name):
    while True:
        num = yield
        print("%s吃了第%s个包子"%(name, num))

c1 = consumer("c1")
c1.__next__()
c2 = consumer("c2")
c2.__next__()
c3 = consumer("c3")
c3.__next__()

for i in range(10):
    c1.send(i)
    c2.send(i)
    c3.send(i)

