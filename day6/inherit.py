# -*- coding:utf-8 -*-
# LC

#class People:  经典类
#class People(object):  新式类

class People(object):

    def __init__(self,name,age,):
        self.name = name
        self.age = age

    def eat(self):
        print("%s is eating"%self.name)

    def sleep(self):
        print("%s is sleeping"%self.name)

    def talk(self):
        print("%s is talking"%self.name)

class Relation(object):     #新式类
    def make_friends(self,obj):
        print("%s is trying to make friends with %s"%(self.name,obj.name))

class Man(People,Relation):      #继承父类,多继承
    def __init__(self,name,age,money):      #对构造函数进行重构
        People.__init__(self,name,age)      #继承父类的参数继承
        #super(Man,self).__init__(name,age)  继承父类的构造函数，与People.__init__(self,name,age)一样，新式类写法
        self.money = money
        print("%s born with %s money"%(self.name,self.money))

    def piao(self):
        print("%s is piaoing"%self.name)

    def sleep(self):            #更新，重构父类方法
        People.sleep(self)
        print("man sleeping ,update")

class Women(People,Relation):   #多继承，多继承在实例在实例化过程中，查找构造函数的时候，先从本类找，如果没有，再从父类找，多继承的话，从继承的父类按左至右找

    def get_birth(self):
        print("birth")

m1 = Man("LC",16,100)
m1.eat()

w1 = Women("Pxm",11)

m1.make_friends(w1)
