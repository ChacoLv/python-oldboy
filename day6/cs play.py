# -*- coding:utf-8 -*-
# LC


class Role:
    def __init__(self,name,role,weapon,life_value=100,money=15000):
        #构造函数
        #在实例化时做一些类的初始化工作
        self.name = name
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money

    def shot(self):
        print("%s shoting..."%self.name)

    def got_shot(self):
        print("%s got shoting"%self.name)

    def find_role(self):
        print("%s role is %s"%(self.name,self.role))

    def buy_gun(self,gun_name):
        print("%s is buying %s"%(self.name,gun_name))
#类实例化

r1 = Role("LC","Terrorist","AK47")
r1.shot()
r1.buy_gun("M4A1")