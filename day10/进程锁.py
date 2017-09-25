from multiprocessing import Lock,Process
import os


def f(l,i):
    l.acquire()             #给进程加锁，给进程加锁的目的是在调用资源的时候，只有加锁的进程才能够调用资源
    print("hello world",  os.getpid(), os.getppid())
    l.release()             #进程解锁



if __name__ == "__main__":
    lock = Lock()
    for i in range(1000):
        p = Process(target=f,args=(lock,i))
        p.start()