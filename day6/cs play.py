# -*- coding:utf-8 -*-
# LC


class Role:
    number = 123   #类变量
    test_list = []
    def __init__(self,name,role,weapon,life_value=100,money=15000):
        #构造函数
        #在实例化时做一些类的初始化工作
        self.name = name            #实例变量（静态属性），作用域就是实例本身
        self.role = role
        self.weapon = weapon
        self.__life_value = life_value      #私有属性
        self.money = money
    def show_status(self):
        print("%s life value is %s"%(self.name,self.__life_value))  #通过调用类的函数进行查看私有属性
    def __show(self):   #私有方法，加两个_
        pass

    def __del__(self):
        #析构函数
        print("%s is die!!!"%self.name)

    def shot(self):#类的方法、功能，（动态属性）
        print("%s shoting..."%self.name)

    def got_shot(self):
        print("%s got shoting"%self.name)

    def find_role(self):
        print("%s role is %s"%(self.name,self.role))

    def buy_gun(self,gun_name):
        print("%s is buying %s"%(self.name,gun_name))
#类实例化

r1 = Role("LC","Terrorist","AK47")          #实例化，生成一个角色，又叫做Role这个类的实例
r1.shot()
r1.buy_gun("M4A1")
r2 = Role("xm","good guy","m4a1")
#实例变量优先于类变量

r1.bullet_prove = True      #可新增实例变量
r1.name = "hell"            #修改实例变量
del r1.name                 #删除实例变量

r1.number = "改类变量"      #改变r1的类变量，只对r1有效

#私有属性查看方法
r1.show_status()

r1.test_list.append("from r1")
r2.test_list.append("from r2")


print(r1.name,r1.number)








