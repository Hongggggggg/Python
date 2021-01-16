#List
names = ["wang", "hong", "xu", "zhao"]
print(names)

#插入 insert
names.insert(1, "gong")
print(names)

#追加 append
names.append("li")
print(names)


#查找
'''查找元素是否在列表内'''
print("xu" in names)
'''查到元素的下标并返回'''
print(names.index("xu"))
'''查找元素的个数'''
print('a的个数:', names.count("a"))


#合并
'''将两个列表合并'''
print("\r\n=========将两个列表合并=======")
names2 = ["sun", "liu", "fen"]
names.extend(names2)
print(names)

#嵌套
'''可以在list里嵌套list'''
print("\r\n=======列表的嵌套===========")
names.insert(3, [1,2,3])
print(names, names[3][2])

#删除
"查到相应的元素并删除"
print("\r\n=========删除元素=======")
'''del'''
del names[-1]
print(names)

'''pop'''
names.pop()#默认弹出最后一个元素
names.pop(3)#弹出指定位置元素
print(names)

'''clear'''
names2.clear()#清空所有元素
print("names2:", names2)

'''remove'''
names.remove("zhao")#从左到右找到第一个匹配的元素并删除
print(names)

#切片
print("\r\n===========切片==========")
print(names[1:4])#list[start:end:step], 不包括list[end],step默认为1
print(names[1:-1])
print(names[1:])
print(names[:-2])
print(names[::2])#设定切片步长为2
print(names[-1:-6:-1])#从右往左切片取值
print(names[::-2])

#反转
print("\r\n===========反转==========")
names.reverse()
print(names[::-1])
print(names)

#排序
print("\r\n===========排序==========")
names.sort()
print(names)

#遍历
print("\r\n===========遍历==========")
for i in names:
    print(i)

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

#字典{key1:value, key2:value2},
#性质：1、key必须不可变 2、可存放多个value,value可以是列表或者其他 3、无序
info = {
    "name":"hong",
    "age":20,
    "job":"eng",
    "weight": 60,
    "salary":1000000,
    "list": [1, 2, 4]}

#打印所有key和value
print(info.keys(), info.values())

#增(若key已经存在则替换，没有则增加)
info["height"] = 188
d = {"name": "hammer", "country": "china"}
info.update(d) #将字典d的键值对添加到info中,有重复则替换
print(info)

#删
info.pop("height")  #删除指定key
info.popitem()      #随便删除一个key
del info["age"]     #同pop
#names.clear()       #清空
print(info)

#查
print(info["name"])
print("age" in info)
print(info.get("age", 10))#不存在则返回10,不设置则返回none
print(info)
print(info.items())#返回一个包含所有键值对的元组的列表
#遍历
for i in info: #推荐
    print(i, info[i])

for i in info.items():
    print(i)

for k,v in info.items():
    print(k,v)

#集合{a, b, c}
a = {1, 2, 3, 3, 2, 'alex', 'hong', 'hong'}#天生去重
print(a)

li = [4, 5, 6, 7, 7, 4]
print(set(li))

a.add(5)#增加元素

#a.add(li)#不可增加可变元素

a.remove(5)# 删除元素
a.discard(5)# 删除元素
a.pop()#随机删
 #集合的关系运算

s_name = {'xiaozhu', 'peiqi', 'ming', 'uzi', 'theshy', 'bin'}
s_other_name = {'faker', 'deft', 'show', 'maker', 'uzi', 'theshy'}
print(s_name & s_other_name)#交集
print(s_name | s_other_name)#并集
print(s_name - s_other_name)#差集
print(s_name ^ s_other_name)#对称差集,删除相同元素后合并
#三种关系：相交，包含，不相交
print(s_name.isdisjoint(s_other_name))#判断是否不相交
print(s_name.issubset(s_other_name))  #判断s_name是否是s_other_name的子集
print({'faker', 'deft'}.issubset(s_other_name))
