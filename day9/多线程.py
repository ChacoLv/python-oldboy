import threading
import time

def run(n):
    print("task",n)
    time.sleep(2)
    print("hello,",n,threading.current_thread())        #查看当前进程信息

# t1 = threading.Thread(target=run,args=("t1",))
# t2 = threading.Thread(target=run,args=("t2",))

# t1.start()
# t2.start()
#  t1.join()

start_time = time.time()
print("Start time ",start_time)

t_obj = []
for i in range(10):
    print(threading.current_thread())
    t = threading.Thread(target=run,args=("task %s"%i,))
    t.setDaemon(True)   #设置为守护线程，设置成守护线程后，主线程可以不等待守护线程执行完成后执行,主线程退出后，守护线程将全退出
    t.start()       #start方法是开始进程
    t_obj.append(t)

print("----------all is ok ",time.time()-start_time,threading.current_thread(),threading.active_count())        #打印当前执行的程序的线程信息，以及活动的线程数量

# for i in t_obj:
#     i.join()        #jion方法表示等待该进程结束，主线程需要等待子进程执行完毕后再进行

time.sleep(5)           #添加个3秒sleep，可以为守护线程创建执行完成时间
print("hello")

