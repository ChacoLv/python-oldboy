# -*- coding:utf-8 -*-
# LC


#类方法
class Dog(object):
    name = "Mark"
    def __init__(self,name):
        self.name = name
    @classmethod
    def eat(self):
        print("%s is eating %s"%(self.name,"banana"))   #name为类变量，而非实例变量

d = Dog("Alex")
d.eat()
#运行结果：Mark is eating banana