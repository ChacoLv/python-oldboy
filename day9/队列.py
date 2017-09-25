import queue


#先进先出队列
'''
q_fifo = queue.Queue(7)      #设置一个先进先出的队列

for i in range(6):
    q_fifo.put(i)

print(q_fifo.queue)
print(q_fifo.qsize())
print(q_fifo.full())

q_fifo.put_nowait(2)            #表示不等待就加入，如果队列慢，则抛出异常
while True:
    print(q_fifo.get())

#print(q_fifo.get())


#后进先出队列

import queue
q_lifo = queue.LifoQueue()

for i in range(4):
    q_lifo.put_nowait(i)

while True:
    print(q_lifo.get(timeout=1))        #延迟1秒，如果get不到数据，则抛出异常
'''
#优先队列


import queue

q_PQ = queue.PriorityQueue()

q_PQ.put({1:"LC"})      #按着元组的第一个元素进行对比，小的优先
q_PQ.put({8:"Jack"})
# q_PQ.put({6:"Mark"})
# q_PQ.put({4:"Joe"})


print(q_PQ.queue[0][1])

#
# print(q_PQ.queue[3])
#
# while q_PQ.qsize():
#     print(q_PQ.get())


