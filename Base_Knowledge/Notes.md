字符串：

- 可做乘法运算：

  ```python
  str = "abcdefg"
  print(str * 3)
  ```

  输出：

  ```python
  "abcdefgabcdefgabcdefg"
  ```

  

- 格式化：

  ```python
  name = "hong"
  age = 18
  msg = '''
  ----------Start----------
  Name: %s
  Age	: %d
  ----------End------------
  ''' % (name, age)
  print(msg)
  ```

   输出：

  ```python
  ----------Start----------
  Name: hong
  Age : 18
  ----------End------------
  ```

  

- 反转

  ```python
  n = "你的名字"
  print(n[::-1])
  ```

  输出：

  ```python
  "字名的你"
  ```




集合：

1、里面的元素不可变，不可存list等可变元素

2、去重，集合里没办法存重复的元素

3、无序、无先后之分，{3，4，5}和{3，5，4}是同一个集合





**1、变量解压**

```python
L = [1,2]
a,b = L
```

当python检测到等号左边是多个变量，右边是list或者tuple之后，会自动执行list和tuple的解压，将它依次赋值给对应的元素

二维数组的遍历也是同样的原理

```python
l = [[1,2], [3,4], [5,6]]
for i,j in l:
	print(i,j)
```

即使是在变量的组合当中也可以生效：

```python
a,b,c = 1,3,(4,5)
print(c)
#输出的结果是（4，5）

a,b,(c,d),e = 1,2,(4,5),7
print(c,d)
#输出结果是4 5
```

缺省元素：

​	当我们获取元素时，元数据中有不需要的字段的时候，可以用_来代表一个缺省值， _对应的数据不会被储存下来，只是为了方便我们凑齐元素。

```python
_,_,(c,d),_ = 1,3,(4,5),7
print(c,d)
#输出结果是4 5
```

再比如，当我们遍历dict的时候，有可能我们并不关注dict的key，只希望获得它的value，这个时候也可以使用缺省符号：

```python
a = {}
for _, v in a.items();
	print(v)
```

**压缩变量**：

```python
data = ['wheel', 'factory1', 3, 4, 5, 6, '2020-02-02']
name, factory, *inch, date = data
print(inch)
#输出[3,4,5,6]
```

也可以使用缺省值_ 过滤数据：

```python
data = ['wheel', 'factory1', 3, 4, 5, 6, '2020-02-02']
name, factory, *_, date = data
```

***的作用**

```python
def func(*args, **kw)
	pass
```

*代表解压数组，**代表解压dict

```python
a = [1,3,5]
print(a)
#输出[1,3,5]
print(*a)
#输出1,3,5
```

​	也就是说前者是将a当成一个数组输出，是一个变量，后者则是将a解压了，当成了3个变量输出。那么同样的道理，kw，也是将作为dict的kw解压，以key: value的形式展开。不过如果你直接调用 kw会得到一个报错，这个操作只能在函数传递参数的时候使用



排序：

1、字典排序：

```python
kids = [
    {'name': 'xiaoming', 'score': 99, 'age': 12},
    {'name': 'xiaohong', 'score': 75, 'age': 13},
    {'name': 'xiaowang', 'score': 88, 'age': 15}
]
```

按照score排序：

```python
sorted(kids, key = lambda x: x['score'])
```

按照score和age排序：

```python
sorted(kids, key = lambda x: (x['score', 'age'])
```

也可用python自带库operator库中的itemgetter函数：

```python
sorted(kids, key = itemgetter('score', 'age'))
```



2、对象排序

```python
class Kid:
    def __init__(self, name, score, age):
        self.name = name
        self.score = score
        self.age = age

    def __repr__(self):
        return 'Kid, name: {}, score: {}, age: {}'.format(self.name, self.score, self.age)

kids = [Kid('xiaoming', 99, 12), Kid('xiaohong', 75, 13), Kid('xiaowang', 88, 15)]
```

使用operator库中的attrgetter函数：

```python
sorted(kids, key = attrgetter('score'))
```

也可以用匿名函数lambda来实现：

```python
sorted(kids, key = lambda x: x.score)
```



3、自定义排序：

因为sorted是从小到大排序的，过程使用的是<=, 所以重载lt函数

将年龄从大到小排序：

```python
class Kid:
    def __init__(self, name, score, age):
        self.name = name
        self.score = score
        self.age = age

    def __repr__(self):
        return 'Kid, name: {}, score: {}, age: {}'.format(self.name, self.score, self.age)

    def __lt__(self, other):
        return self.age > other.age

sorted(kids)
```

将分数从大到小，分数相同则按年龄从小到大排列：

```python
    def __lt__(self, other):
        return self.score > other.score or (self.score == other.score and self.age < other.age)
```

