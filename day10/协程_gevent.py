import gevent

def func1():
    print("hello world test 1...")
    gevent.sleep(2)                 #通过gevent来实现自动的进程切换，模拟遇到IO操作 
    print("hello world test2 .......")

def func2():
    print("hello jack test 1......")
    gevent.sleep(1)
    print("hello jack test 2............")

def func3():
    print("hello mark test 1.....")
    gevent.sleep(1.5)
    print("hello mark test 2..........")

gevent.joinall([
    gevent.spawn(func1),
    gevent.spawn(func2),
    gevent.spawn(func3)
])