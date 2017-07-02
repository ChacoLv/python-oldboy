# -*- coding:utf-8 -*-
# LC

# 函数即"变量"
# 高阶函数
#     a.把一个函数名当做实参传给另一个函数(在不修改被装饰函数的源代码的情况下，为其添加功能)
#     b.返回值中包含函数名（不修改函数的调用方式）
'''
import  time
def bar():
    print("in the bar!")
    time.sleep(2)

def foo(func):
    start_time = time.time()
    func()                  #根据内存地址，执行代码
    stop_time = time.time()
    print("run time %s"  %(stop_time-start_time))
foo(bar)

#函数嵌套，是在一个函数内，用一个def来定义一个新的函数
def foo():
    print("in the foo")
    def bar():
        print("in the bar")
    bar()

#函数调用
def foo():
    print("in the foo")
    bar()

def bar():
    print("in the bar")

#装饰器
import time
def deco(func):
    def wraper(*args):
        start_time = time.time()
        func(*args)
        stop_time = time.time()
        print("running time is:",stop_time - start_time)
    return wraper

@deco       #等于test1 = deco(test1) 返回值为wraper的内存地址，即test1等于wraper,所有*args同样可以传递给wraper
def test1(*args):
    print("test1".center(30,"-"))
    print("values is",*args)
test1(1,2,3)


user = "jack"
def auth(auth_type):
    def outer_wraper(func):
        def wraper(*args,**kwargs):
            if auth_type=="local":
                username = input("username:").strip()
                if user == username:
                    print("success!")
                    res = func()
                    return res
                else:
                    print("invalid input")
        return wraper
    return outer_wraper

@auth(auth_type="local")    #即这里多了一个参数，这个参数需要传递给auth函数，多了这个参数可以再装饰器内加判断
def home():
    print("home page")

home()
'''
#匿名函数

calc = lambda a,b :a+b
print(calc(1,2))

calc = lambda n : 3 if n<5 else n*n
print(calc(12))

res = filter(lambda n:n>5,range(10))
res = map(lambda n:n*n,range(5))
for i in res:
    print('----',i)

res = [lambda i:i*2 for i in range(10)]







