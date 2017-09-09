import threading,time



def run(n):
    semaphore.acquire()
    time.sleep(1)           #通过sleep 1s，可以看见一次有5个进程一起执行
    print("running the thread %s"%n)
    semaphore.release()





if __name__ == '__main__':
    semaphore = threading.BoundedSemaphore(5)           #同时有5个线程进行任务执行
    for i in range(20):
        t = threading.Thread(target=run,args=(i,))
        t.start()


while threading.active_count() != 1:
    pass#print(threading.active_count())
else:
    print("all is ok")