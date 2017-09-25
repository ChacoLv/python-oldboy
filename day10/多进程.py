
import time
import multiprocessing
import threading
import os
import psutil


def run(name):
    print("hello",name)
    time.sleep(2)
    print("父进程",os.getppid(),psutil.Process(os.getppid()))
    print("子进程",os.getpid(),psutil.Process(os.getpid()))
    print("子进程", os.getpid(),psutil.Process(os.getpid()))


if __name__ == "__main__":
    for i in range(3):
        print("pid",os.getppid())
        print("ppid",os.getpid(),psutil.Process(os.getppid()))
        p = multiprocessing.Process(target=run,args=("Jack",))
        p.start()



