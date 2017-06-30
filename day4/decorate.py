import time

def deco_1(func):
    def wraper(a,b):
        print("this is deco_1")
        func(a,b)
    return wraper

def deco_2(func):
    def wraper(a,b):
        print("this is deco_2")
        func(a,b)
    return wraper

@deco_1
@deco_2
def myfunc(x,y):
    print("this is myfunc")
    total = x + y
    print("sum is ",total)
myfunc(1,2)

