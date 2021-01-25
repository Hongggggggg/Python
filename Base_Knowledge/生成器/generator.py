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
