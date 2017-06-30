# -*- coding:utf-8 -*-
# LC

#byte类型

msg="我你"
print(msg)
print("-------------",msg.encode(encoding="utf-8"))
print(msg.encode(encoding="utf-8").decode(encoding="utf-8"))

#列表复制：

name = ["lc","pxm",["alex","jack"],"pt"]
print(enumerate(name))
name2 = name.copy()                       #列表复制，复制为浅copy，不会复制列表内的列表
print(name)
print(name2)
name[2][0]="ALEXANDER"
print(name)
print(name2)

#列表深入copy
import copy
name = ["lc","pxm",["alex","jack"],"pt"]
name2 = copy.deepcopy(name)
print(name)
print(name2)
name[2][0]="ALEXANDER"
print(name)
print(name2)
'''
'''
#列表切片
print(name[1:3])                     #切片
print(name[:3])
print(name[-1])                      #取最后一位
print(name[-2:])                     #取最后两位

#列表增加
name.append("huanglei")             #最后添加一个对象
name.insert(1,"xulingling")        #在指定的位置插入一个对象

#列表删除
name.remove("lvcheng")             #直接删除，删除指定对象
del name[1]
name.pop(1)                         #默认删除最后一个对象，指定位置删除

#列表修改
name[1]="smq"
print(name)

#列表操作
name.index("smq")                   #查找对象对应的位置
name.count("lvcheng")              #统计列表中对象的出现的次数
name.reverse()                       #列表反转
name.sort()                          #列表排序，按着ASCII来的
name2 = [1,2,3]
name.extend(name2)                   #列表扩展，即将另一个列表扩展至列表
name.clear()                         #清空列表
del name2                            #删除列表


name = ["lc","pxm",["alex","jack"],"pt","ggg","dex","fed","fck"]
#步长切片
print(name[0:-1:2])                         #表示打印列表中的从多少开始至多少结束，最后一个表示间隔
print(name[::2])
#列表循环
for i in name:
    print(i)

import copy
name = ['username',['age','18']]

p1=name[:]
p2=name.copy()
p3=copy.copy(name)
p4=list(name)
p5=name

p1[0]='Tom'
p2[0]='alex'
p3[0]='pxm'
p4[0]='chaco'
name[0]='peter'
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)








