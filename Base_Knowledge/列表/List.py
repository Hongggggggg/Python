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

#列表生成器
a = [1, 2, 3, 4, 5]
a = [a ** a for i in a]
print(a)
