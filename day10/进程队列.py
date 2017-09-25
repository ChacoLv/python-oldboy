import multiprocessing
import time
import os
import psutil


def que(name):
    name.put("hello que")               #向父进程中复制过来的进程进行操作
    name.put("32")
    # print('===',os.getppid())
    # print(os.getpid())

if __name__ == "__main__":
    # print(os.getppid(),psutil.Process(os.getppid()))
    q = multiprocessing.Queue()
    q.put("11111")
    # print(os.getppid(),psutil.Process(os.getppid()))
    p1 = multiprocessing.Process(target=que,args=(q,))
    # p1 = multiprocessing.Process(target=que,args=(q,))
    # print(os.getpid())
    p1.start()
    p1.join()
    q.put("222")
    print(q.get())
    print(q.get())
    print(q.get())
    print(q.get())

#进程之间为什么能够用queue实现通信？？？？？？？？



