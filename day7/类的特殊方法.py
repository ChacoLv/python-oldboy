# -*- coding:utf-8 -*-
# LC

#__doc__ 输出类的描述信息
class Foo:
    '''
    类的描述信息
    '''
    def func(self):
        pass

print(Foo.__doc__)


#__module__ 输出当前操作的对象在那个模块
#__class__  输出当前操作的对象的类是什么

from lib.aa import C
obj = C()
print(obj.__module__)
print(obj.__class__)

#__call__ 对象后加括号，触发执行
#构造方法的执行是由创建对象触发的，即：对象=类名();而对于__call__方法的执行是由对象加括号触发的，即对象()或类()()
class Dog(object):
    def __init__(self,name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print("%s running call"%self.name,args,kwargs)

obj2 = Dog("alex")
obj2("wawawa",sex="F")


#__dict__ 查看类或者对象中的成员

print(Dog.__dict__)
print(obj2.__dict__)

#__str__  如果一个类中定义了__str__方法，则在打印对象的时候，默认输出该方法（__str__）的值
class Cat(object):
    def __str__(self):
        return "str method"

obj3 = Cat()
print(obj3)

#__getitem__,__setitem__,__delitem__  用于索引操作，如字典，分别进行获取，设置，删除数据

class apple(object):
    def __init__(self):
        self.data = {}
    def __getitem__(self, key):
        print("get apple %s"%key)
        return self.data.get(key)
    def __setitem__(self, key, value):
        print("setting apple,%s,%s"%(key,value))
        self.data[key] = value
    def __delitem__(self, key):
        print("deleting apple %s"%key)
        del self.data[key]

obj4 = apple()
obj4["apple1"] = "red"
obj4["apple2"] = "green"

res = obj4["apple1"]
print('---',res)
print(obj4.data)
del obj4["apple1"]
res = obj4["apple2"]        #删除后则没有了。输出为None，具体是否删除，也是由__delitem__方法定义的
print('---',res)


#__new__
class Foo(object):
    def __init__(self,name):
        self.name = name

f = Foo("Jack")
print(type(f))
print(type(Foo))




