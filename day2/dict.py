# -*- coding:utf-8 -*-
# LC

dict = {
    'stu1101':"Peter",
    'stu1102':"Jack",
    'stu1103':"Alex",
}
print(dict)
print(dict.values())            #打印字典里的值
print(dict.keys())              #打印字典里的key

dict.setdefault("stu1105","LC")     #如果key存在，则返回原有的值，如果key不存在，则添加key和相应的值到字典里
print(dict)

dict2 ={
    "stu1101":"GL",
    1:2,
    3:5,
}
dict.update(dict2)              #更新字典，如果dict2中的key在dict中存在，则更新dict中key对应的值，如果没有，则添加至dict中
print(dict)

print(dict.items())         #将字典变成一个列表


c = dict.fromkeys(["LC","HL","GL"],["classmate",{"Name":"XLL"},"19"])       #前面为key，后面赋值给key，如果修改Value，则会所有改
print(c)
c["LC"][1]["Name"]="Xlingling"
print(c)

#字典循环
for i in dict:              #i表示字典里的key
    print(i,dict[i])



#查找
dict1 = dict['stu1101']         #查找，但必须确认key值是存在，否则会报错
dict.get('stu1101')     #查找，如果不存在key，则返回None
dict2 = 'stu1101' in  dict      #如果在字典内，则返回True，否则为Fasle

dict["stu1101"]="Will"         #修改字典
dict["stu1104"]="Mark"          #增加，如果key在字典中没有，则添加

#删除
del dict["stu1101"]     #删除字典key和值
dict.popitem()              #随机删除
dict.pop("stu1102")     #删除指定key和值
'''
#多层字典嵌套
'''
dict ={
    "Europe":{
        "Denmark":["child","pipe"],
        "Germany":["moto","Volk"],
        "Net":["flower","girl"]
    },
    "ASPA":{
        "China":["people","money"],
        "Japan":["beautiful girl","Toyota-hot"]
    },
    "Americam":{
        "North":["write","black"],
        "East":["basketball","football"]
    }
}
dict["Europe"]["Net"]=["wind","farmer"]         #修改嵌套字典信息
print(dict)







