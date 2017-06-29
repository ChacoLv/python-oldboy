# -*- coding:utf-8 -*-
# LC



#函数即"变量"
#高阶函数
    #a.把一个函数名当做实参传给另一个函数(在不修改被装饰函数的源代码的情况下，为其添加功能)
    #b.返回值中包含函数名（不修改函数的调用方式）

# import  time
#
# def bar():
#     print("in the bar!")
#     time.sleep(2)
#
# def foo(func):
#     start_time = time.time()
#     print(func)             #打印传递过来函数的"门牌号",即内存地址
#     func()                  #根据内存地址，执行代码
#     stop_time = time.time()
#     print("run time %s"  %(stop_time-start_time))
#
# foo(bar)
#
# #函数嵌套，是在一个函数内，用一个def来定义一个新的函数
# def foo():
#     print("in the foo")
#     def bar():
#         print("in the bar")
#     bar()
#
# #函数调用
# def foo():
#     print("in the foo")
#     bar()
#
# def bar():
#     print("in the bar")
#
# #装饰器
import time












