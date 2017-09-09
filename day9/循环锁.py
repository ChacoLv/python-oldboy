import threading,time

def run1():
    print("this is run1")
    lock.acquire()
    global num1
    num1 += 1
    lock.release()
    return num1

def run2():
    print("this is run2")
    lock.acquire()
    global num2
    num2 +=1
    lock.release()
    return num2




def run3():
    lock.acquire()
    res1 = run1()
    print("this is between run1 and run2")
    res2 = run2()
    lock.release()
    print(res1,res2)




if __name__ == '__main__':
    num1,num2 = 0,0
    lock = threading.RLock()                #循环锁可以防止锁中带锁，锁中锁无法释放自己的锁
    for i in range(10):
        t = threading.Thread(target=run3)
        t.start()

while threading.active_count() != 1:
    print(threading.active_count())
else:
    print(num1,num2)

#循环锁用于锁中还有锁的情况使用，防止锁中锁被锁死无法出来。