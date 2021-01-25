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

#集合生成器
some_list = [1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 8, 9, 9]
even_set = {x for x in some_list if x % 2 == 0}
print(even_set)


