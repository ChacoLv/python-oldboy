# -*- coding:utf-8 -*-
# LC
'''
# 列表生成式
def func(x):
    print(x)
    return 2*x
print([ func(i) for i in range(10) ])

a = [ i*2 for i in range(1000000000000)]        #此列表生成式会占用大量内存空间，在没有调用的情况下，列表已经存在于内存中
len(a)
# 生成器
b = ( i*2 for i in range(1000000000000))        #生成器，只有在调用b的时候，才会按着规则进行运算，将结果返回给b，使用的时候才占用内存，速度快
#生成器不支持切片
b[100]      #这种无法直接取出来
for i in b:
    print(i)

#生成器
#1.只有在调用的时候，才会生成相应的数据
#2.只记录当前的位置
#3.只有一个__next()__方法
'''

#fibnacci函数
#函数生成器，使用yield,用了yield的函数，就不在是一个函数，而是一个生成器
def fib(max):
    n,a,b = 0,0,1
    while(n<max):
        n += 1
        yield b                 #yield是会返回当前值给函数，执行一次,__next__方法会调用yeild值
        a,b = b,a+b
    return "---done---..."
from collections import Iterator

f = fib(9)
print("-------",isinstance(f,Iterator))
while True:
    try:
        g = f.__next__()
        print("function generator:",g)
    except StopIteration as e:
        print("Generator is stop,value is ",e.value)
        break
#send 会唤醒当前生成器，并传递一个值给yeild
'''
def consumer(name):
    print("%s 准备开始吃包子了"%name)
    while True:
        baozi = yield
        print("包子{%s}来了，{%s}请吃吧!"%(baozi,name))

def producer(name):
    c1 = consumer("A")              #此步骤仅是将函数变成生成器，而生成器不会执行，如果要执行则需要调用__next__方法，__next__方法遇到yield则中断
    c2 = consumer("B")
    next(c1)        #等于c1.__next__()方法
    next(c2)
    print("%s 做包子了"%name)
    for i in range(6):
        print("包子[%s]好了，分成两份"%i)
        c1.send(i)
        c2.send(i)
        

producer("lvcheng")

#1. 函数的执行流程是按着顺序执行，遇到return和最后一行的时候函数才结束执行，生成器是在每次调用__next__()的时候，在遇到yield语句的时候返回，并在下一次调用的时候，继续在上一次yield执行的位置继续
#2. 可以通过for循环的对象称为可迭代对象,可以通过isinstance()判断一个对象是否为可迭代对象,列表，元组，字典，字符串都是可迭代对象，而整数则不是
from collections import Iterable            #导入Iterable可以判断一个对象是否为可迭代对象
print(isinstance([],Iterable))          #True
print(isinstance({},Iterable))          #True
print(isinstance((),Iterable))          #True
print(isinstance("abcd",Iterable))      #True
print(isinstance((x for x in range(10)),Iterable))  #True
print(isinstance(100,Iterable))         #False

#迭代器
#1. 可以被next()函数调用并不断返回下一个值的对象称为迭代器
#2. 可以同isinstance()判断一个对象是否是Iterator
#3. 生成器都是迭代器,但列表，字符串，字典等不是迭代器，可以使用iter()函数变成迭代器
from collections import Iterator
print(isinstance((x for x in range(10)),Iterator))      #True
print(isinstance([],Iterator))          #False
print(isinstance(iter([]),Iterator))        #True
'''

