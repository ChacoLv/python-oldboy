# -*- coding:utf-8 -*-
# LC

import time
#函数：
def logger():               #定义日志函数
    time_format = '%Y-%m-%d  %X'        #定义时间格式
    time_current = time.strftime(time_format)       #抓取当前时间
    with open("log_file","a") as f:
        f.write("%s this is end\n"%time_current)

def func1():
    """to declare the function"""           #说明这个函数是做什么的
    print("this is function1")              #函数工作模块，逻辑
    logger()
    return 0                                    #函数返回值

#过程：                #过程是没有返回值的函数，在python中，过程默认返回None
def func2():
    """function 2"""
    print("this is function2")
    logger()
    return 1,{"name":"lvcheng","age":"18"}      #可返回多个值

x = func1()             #调用函数
y = func2()
print(x)
print(y)

def func3(x,y,z):              #x,y为形参，同为位置参数
    print(x,y,z)
    return x,y,z

func3(1,2,3)          #位置参数调用，位置需要与形参一一对应
func3(1,2,z=3)
func3(y=2,z=3,x=1)      #关键字调用，关键参数，与形参顺序无关

#默认参数
def func4(x,y=3):        #y是默认参数
    print(x)
    print(y)
func4(1)
func4(1,5)
#默认参数可以不传递，如果有传递，则是传递的值
#用途 1,默认安装的时候，2, 链接数据库的端口号等

#参数组,对于实参不固定函数的实现
def func5(*args):       # *是关键字，元组的方式传递
    print(args)

# *args接受N个位置参数，转换成元组的方式

test1 = func5(1,2,3,4,5)    # 1,2,3,4,5以(1,2,3,4,5)元组的方式传递给args
test1 = func5(*[1,2,3,4])

#参数组，以字典的方式实现

def func6(**kwargs):
    print(kwargs)
    print(kwargs['name'])       #取字典里的值
    print(kwargs['age'])
# **kwargs接收N个关键字参数，转换成字典的方式传递


test2 = func6(name="lc",age=9)          #必须传递关键字参数
test2 = func6(**{"name":"lc","age":10})


def func7(name,age=19,**kwargs):        #有形参，有默认参数，有参数组
    print(name)
    print(age)
    print(kwargs)

test3 = func7("lc",21,sex="M",hobby="girl")
test3 = func7("lc",sex="M",hobby="girl",age = 32)

def func8(name,age=19,*args,**kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)

func8("lc",2,3,4,sex="M",hobby="money")

#局部变量
def change_age(age):
    global name             #函数内申明全局变量，全局生效
    print("before age",age)
    age = 18                 #局部变量,这个函数就是这个变量的作用域
    name = "LLL"
    print("after change age",age)

age = 20
name = "LC"
print("!!!name",name)
change_age(age)
print(age)
print("name:",name)


#字符串，整数，元组在局部变量不能修改；列表，字典，集合，类在局部能够修改全局变量
names = ["LC","Jack","Ma"]
def change_name():
    names[0] = "Lucy"
    print(names)
print(names)
change_name()
print(names)

#递归函数
def calc(n):
    print(n)
    if int(n/2)>0:
        return calc(int(n/2))

calc(10)

#递归函数特性
#1. 递归行数必须有明确的结束条件，2. 递归函数没进行一次递归，问题规模相对之前会减少，3.递归效率不高



#函数默认可以没有返回值，没有返回值则返回为None
#函数可以有多个返回值，类型可以不同，但其实多个返回值整体上是一个元组
#关键参数不能够写在位置参数前面
#局部变量只在函数内部生效，这个函数就是这个变量的作用域
#字符串，整数，元组在局部变量不能修改；列表，字典，集合，类在局部能够修改全局变量
