# -*- coding:utf-8 -*-
# LC
class Dog(object):
    def __init__(self,name):
        self.name = name

    def eat(self):
        print("%s is eating"%self.name)

def bulk(self):
    print("%s is yelling"%self.name)


d = Dog("Jack")

choice = input(">>:").strip()
print(hasattr(d,choice))            #表示对象中是否含有choice的属性，包含变量，方法等

if hasattr(d,choice):
    print(getattr(d,choice))        #获取对象中的choice属性，如果是变量，则获取变量值，如果是方法，可以通过加()进行执行
    getattr(d,choice)()
else:
    setattr(d,choice,bulk)          #设置对象中的choice属性，如可以新增一个变量或方法
    getattr(d,choice)(d)        #func = get(d,choice), func(d)
d.talk(d)

delattr(d,choice)               #删除对象中的choice属性，可以是变量，也可以是方法
d.talk(d)


