# -*- coding:utf-8 -*-
# LC

class Dog(object):
    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print("%s is eating %s"%(self.name,food))

d = Dog("Jack")
d.eat("banana")

#静态方法写法
class Dog(object):
    def __init__(self,name):
        self.name = name
    @staticmethod
    def eat(self):  #需要传进来的是实例了，而不能调用类本身的属性
        print("%s is eating %s"%(self.name,"banana"))

d = Dog("Alex")
d.eat(d)        #传入实例化后的一个实例