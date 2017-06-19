# -*- coding:utf-8 -*-
# LC

list_1 = [1,2,5,2,4,1,9,5]
set_1 = set(list_1)     #集合是无序的，消重的
print(set_1,type(set_1))

set_2 = set([1,3,4,34,9])
print(set_1,set_2)

#集合交集
print(set_1.intersection(set_2))
print("交集:",set_1 & set_2)

#并集
print(set_1.union(set_2))
print("并集:",set_1 | set_2)

#差集
print(set_1.difference(set_2))
print(set_2.difference(set_1))
print("差集:",set_1-set_2)    #in set 1 but not in set 2

#子集
print(set_1.issubset(set_2))

#父集
set_3 = set([32,33])
print(set_1.issuperset(set_3))

#对称差集，即将两个集合中都没有的取出来
print(set_1.symmetric_difference(set_2))
print("对称差集:",set_1 ^ set_2)

#判读两者是否有交集，如果没有交集，则返回True
set_1 = {1,2,5,2,4,1,9,5}
set_3 = {32,33}
print(set_1.isdisjoint(set_3))


#集合基础操作
#添加一项
set_1.add(999)
print(set_1)
#添加多项
set_1.update([888,333,222])
print(set_1)
#删除一项
set_1.remove(999)
print(set_1)
#集合的长度
print(len(set_1))
#判读子字符串，列表，集合，字典是否再里面
99 in set_1      #测试 x是否再集合set_1内部
set_3 >= set_1      #测试集合set_1中的每个元素是否都在set_2中
set_1.copy()        #浅复制


print(set_1.pop())         #随意删除一个元素，并弹出相应元素的值
set_1.remove("element")      #删除指定的元素，如果不存在，则报错，

set_1.discard("element")    #删除指定的元素，如果不存在，则返回None，如果存在，则删除元素