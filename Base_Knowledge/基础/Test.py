
#三元表达式
name__test = "Eva"
sex = "Female" if name__test == "Eva" else "Male"
print(sex)


#元组=只读列表
#元组本身不可变，如果元组中包含其他可变元素，则这些元素可以改变
data = (1, 2, 3, 4, [5, 6, 7], 8, 9)
print(data)
data[4][0] = 10
print(data)
#元组只是存每个元素的内存地址

#==============================================
#字符串 == 不可变列表
name_string = "hongjunyi"
#索引
print(name_string[0])
#切片
print(name_string[1:5])
print(name_string[::-1])

#首字母大写 #全变大写upper
name_string.capitalize()
print(name_string)

#字符串变小写
name_string.casefold()#lower() 
print(name_string)

#统计字符
print(name_string.count("n", 1, 8))

#判断字符串以什么结尾
print(name_string.endswith('i'))

#判断字符串以什么开始
print(name_string.startswith('h'))

#寻找字符
print(name_string.find("g", 1, 8))#返回下标
print(name_string.index("g", 1, 8))#返回下标

#格式化
print("abc {num}, {name}".format(num = 10, name = "hong"))

#判断是否为整数
print("12".isdigit(), "ab".isdigit())

#判断是否为空格
print("".isspace(), " ".isspace())

#拼接
n = ["a", "b", "c"]
print("".join(n))
print("-".join(n))

#去除两边多余字符
n = " ab c "
print(n.strip())#删除两边空格，中间不删 rstrip, lstrip

#替换
n = "my age is 25"
print(n.replace("25", "18"))#count参数为替换次数，默认为none，表示全部替换

#分割并转化为list（元素均为字符串）
print(n.split(" ", 2))#可选分割几次，默认全分 rsplit从右开始

#补0
print(n.zfill(30))

#浅copy,只copy第一层
info2 = info.copy()

#深copy,info2与info完全独立
import copy
info2 = copy.deepcopy(info)

import chardet
#编码与解码
s = "编码与解码"
s = s.encode("utf-8")#以utf-8编码成二进制
print(chardet.detect(s))
print(s)
s = s.decode("utf-8")#将二进制解码成utf-8形式
print(s)
#编码转换，需先转成unicode，再转成目标编码
#utf-8->unicode->gbk
#s = s.encode("unicode")#将二进制解码成utf-8形式
#print(s)

#函数的关键参数
def register(name, age, country):
    print(name)
    print(age)
    print(country)
    return 1,2,3,4,5#返回多个值会当成元组输出

print(register(age = 18, name = "xiaoming", country = "CN"))#关键参数顺序可以任意

#非固定参数
def join(name, age, *args, **kwargs):#*args代表元组，**kwargs代表字典, 位置参数传入args，关键参数传入kwargs
    print(args, kwargs)
    print(args[0], kwargs.get("sex"))

join("xiaoming", 18, "CN", 100, sex = "M")

#全局变量
global_var = [1, 2, 3]

def test():
    a = 10
    b = [1, 2, 3]
    #global_var = 3 这里会报错,不能对全局变量本身进行操作
    global_var.append(4)#当全局变量是列表、字典等，在函数内部是可以对其进行操作的，因为是直接对全局变量地址里的具体内容进行操作
    print(global_var)
    print(locals())#打印函数内所有局部变量
    #print(globals())#打印所有全局变量

test()

#嵌套函数
name = "xiaoming"
def change():
    name = "xiaoming_change"
    def change1():
        name = "xiaoming_change1"
        print(name)

    change1()#只能在change()内部进行调用
    print(name)

change()
print(name)

#匿名函数
calc = lambda x, y : x**y
print(calc(2, 8))

res = map(lambda x:x**2, [1, 3, 5, 7, 9])#map作用是将可迭代内容传入函数依次执行
for i in res:
    print(i)


#高阶函数
def add_1(n):
    return n + 1

def sum(x, y, f):
    return f(x) + f(y)

print(sum(5, 6, add_1))

#python内置函数
a = [1, 2, 3]
print(all(a))#可迭代对象a中所有元素都为True，则all(a)返回True
print(any(a))#可迭代对象a有任意元素为True，则any(a)返回True
a.append(0)
print(all(a))#可迭代对象a中并非元素都为True，则all(a)返回False
a.clear()
print(any(a))#可迭代对象a所有元素全为False，则any(a)返回False

chr(90)#返回数字对应的ASCII字符
dir(a)#返回对象可调用的属性
divmod(4, 2)#返回除法的商和余数（2，0）
eval_list = eval("['alex', 'snow', 'jack']")#将字符串转换成对应类型
print(eval_list, type(eval_list))
exec("print('Hello world')")#将字符串转换成程序执行
filter_list = filter(lambda x:x>10, [0, 12, 34, 35, 2, 1, 55, 7, 9])#对list、dict、set、tuple等可迭代对象进行过滤
print(list(filter_list))
id(filter_list)#查看内存地址
print(isinstance(eval_list, list))#判断数据结构的类型
#iter()待更新
map(lambda x:x**2, [1, 3, 5, 7, 9])#map作用是将可迭代内容传入函数依次执行
print(max([1,2,3]))
print(min([1,2,3]))
a = [1, 2, 3, 4]
b = ['a', 'b', 'c', 'd', 'e']
print(list(zip(a, b)))#将多个列表拼成一个，多余的裁剪掉

#python技巧

