# -*- coding:utf-8 -*-
# LC

class MyType(type):
    def __init__(self,*args,**kwargs):
        print("Mytype init",args,kwargs)
    def __call__(self, *args, **kwargs):
        print("Mytype call",args,kwargs)
        obj = self.__new__(self)
        self.__init__(obj,args,kwargs)



class Foo(object):
    __metaclass__ = MyType      #表示该类是由谁来实例化自己的（即Foo类）
    def __init__(self):
        print("foo init")
    def __new__(cls, *args, **kwargs):
        print("foo new")
        return object.__new__(cls)

f = Foo()
#在python2或者3中，执行顺序为：__new__ ,  __init__,  __call__、
#__new__优于__init__执行
#__call__用于创建__new__

from class_mod import Dog
d = Dog("alex")


