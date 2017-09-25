import time,threading
import queue


q = queue.Queue(maxsize=10)           #实例化一个队列，为生产的产品

def Producer(name):             #定义一个生产者的方法，生产包子
    count = 0
    while True:
        count +=1
        q.put(count)
        print("%s 生产了包子%s"%(name,count))
        time.sleep(1)



def Consumer(name):             #定义一个消费者的方案，消费包子
    while True:
        print("\033[42;1m%s 消费了包子%s\033[0m, 队列长度%s"%(name,q.get(),q.qsize()))
        time.sleep(1)

p1 = threading.Thread(target=Producer,args=("Jack",))
p2 = threading.Thread(target=Producer,args=("Joe",))
c1 = threading.Thread(target=Consumer,args=("Mark",))
c2 = threading.Thread(target=Consumer,args=("LC",))


p1.start()
p2.start()
c1.start()
c2.start()