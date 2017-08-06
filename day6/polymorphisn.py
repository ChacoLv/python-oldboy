# -*- coding:utf-8 -*-
# LC
class Animal(object):
    def __init__(self,name):
        self.name = name
    @staticmethod           #使用装饰器配合实现
    def animal_talk(obj):  # 多态的实现方式，一种接口，多种形态
        obj.talk()

class Dog(Animal):
    def talk(self):
        print("%s is Wooling"%self.name)

class Cat(Animal):
    def talk(self):
        print("%s is Mewing"%self.name)

D1 = Dog("dog1")
C1 = Cat("cat1")

D1.talk()
C1.talk()

def animal_talk(obj):       #多态的实现方式，一种接口，多种形态
    obj.talk()

animal_talk(D1)
animal_talk(C1)

Animal.animal_talk(D1)
Animal.animal_talk(C1)

