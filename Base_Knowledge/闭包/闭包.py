def outer():
    name = 'alex'
    
    def inner():
        print("inner里打印外层函数的变量", name)
    
    return inner

fun = outer()

fun()
'''
正常情况下，outer执行后，内部申请的内存应该已经释放掉了，inner和name都应该被回收
但由于闭包情况的存在，导致我们还是可以调用inner
闭包的意义：返回的函数对象，不仅仅是一个函数对象，在该函数外还包裹了一层作用域，这使得该函数无论在何处调用，优先使用自己外层包裹的作用域
'''

#例子：计算一个数的n次幂
def nth_power(base, exponent):
    return base ** exponent

def nth_power_new(exponent):
    def exponent_of(base):
        return base ** exponent
    return exponent_of


#计算2，3，4的2次方
#不使用闭包：
print(nth_power(2, 2))
print(nth_power(3, 2))
print(nth_power(4, 2))

#使用闭包
square = nth_power_new(2)
print(square(2))
print(square(3))
print(square(4))
