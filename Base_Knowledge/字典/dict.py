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


#字典生成器,key为[0,10)，value为bool
d = {x : x % 2 == 0 for x in range(1, 11)}
print('Dict:', d)
