from multiprocessing import Process,Pool
import os,time

def Foo(num):
    time.sleep(2)
    print("os pid",os.getpid(),"os ppid = ",os.getppid())
    return num + 100

def Bar(arg):
    print("Foo exec done",arg)
    print("bar process id",os.getpid())


if __name__ == "__main__":
    pool = Pool(5)                      #表示最多有多少个进程可以同时使用CPU资源

    print("main process id is ",os.getpid())
    for i in range(10):
        #pool.apply_async(func=Foo,args=(i,))       #表示异步进行，即以进程池最大的数量同步进行
        #pool.apply(func=Foo,args=(i,))              #表示串行执行，即执行一个进程后，再执行下一个进程
        pool.apply_async(func=Foo,args=(i,),callback=Bar)           #callback 是回调，即只有在func执行完毕后，才执行callback，callback调用将由主进程自己调用

    print("end====")

    pool.close()
    pool.join()            #必须要先close，再join，如果将这行注释掉，则程序直接运行结束