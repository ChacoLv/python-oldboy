# -*- coding:utf-8 -*-
# LC
'''
class Dog(object):
    def __init__(self,name):
        self.name = name
        self.__food = None
    @property
    def eat(self):
        print("%s is eating %s"%(self.name,"banana"))
    @eat.setter
    def eat(self,food):
        print("set food:",food)
        self.__food = food

d = Dog("Alex")
d.eat       #属性方法输出的是属性，不需要动态调用，即不需要d.eat()
'''
class Dog(object):
    def __init__(self,name):
        self.name = name
        self.__food = None
    @property
    def eat(self):
        print("%s is eating %s"%(self.name,self.__food))
    @eat.setter
    def eat(self,food):             #修改属性方法的参数
        print("set food:",food)
        self.__food = food
    @eat.deleter        #删除属性方法的参数
    def eat(self):
        del self.__food
        print("deleted!!!!!")

d = Dog("Mark")
d.eat
d.eat = "apple"         #向属性方法种传递参数
d.eat
del d.eat               #删除属性方法种的参数
d.eat




