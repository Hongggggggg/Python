#可以直接作用于for循环的对象统称为可迭代对象：Iterable
#使用isinstance()判断一个对象是否是Iterable对象

from collections import Iterable
from collections import Iterator

print(isinstance([], Iterable))#列表

print(isinstance({}, Iterable))#字典

print(isinstance('abc', Iterable))#字符串

print(isinstance((x for x in range(10)), Iterable))#生成器

print(isinstance(1, Iterable))#整数

#可以被next()调用并不断返回下一个值的对象称为迭代器：iterator 约等于生成器
#生成器都是Iterator，list、dict等虽然是Iterable,但不是Iterator
#可使用iter()把list、dict、str等变成Iterator
print(isinstance([], Iterator))#列表

print(isinstance({}, Iterator))#字典

print(isinstance((x for x in range(10)), Iterator))#生成器

print(isinstance(iter([]), Iterator))#列表

print(isinstance(iter([]), Iterator))#列表
