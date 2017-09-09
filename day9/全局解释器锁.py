import threading
import  time

num = 0
def run():
    lock.acquire()          #配合release使用，即再acquire和release之间加锁了，防止线程未完成，数据没有写入导致不同步，此问题只有在python2中才有。
    global num
    num +=1
    time.sleep(1)
    lock.release()

t_list = []
lock = threading.Lock()         #给任务线程加锁
for i in range(50):
    t = threading.Thread(target=run)
    t.start()
    t_list.append(t)

for j in t_list:
    j.join()



print("num:",num)