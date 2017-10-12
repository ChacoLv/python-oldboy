import socket
import queue
import select


server = socket.socket()
server.setblocking(False)           #设置socket为不阻塞状态，即accept在没有连接接入的时候，会报错，


server.bind(("localhost",9000))           #socket服务器绑定提供服务的地址和端口信息

server.listen(100)      #socket服务器端开启监听


inputs = [server,]
outputs = []

msg_quenes = {}

print("using select to do multi-process !")
while True:
    readable,writeable,exceptional = select.select(inputs,outputs,inputs)   #select中的三个参数分别表示通过select来监控的列表，第一个为要监控的socket的列表并返回给readable，
                                                                            #第三个为要监控的socket并返回给exceptional列表
    for r in readable:
        if r is server:         #表示监控的是服务器本身，还没有新的客户端socket连接进来，在此则需接受新的连接
            conn,addr = r.accept()          #表示接受新的客户端socket连接请求
            print("new socket conn client information %s "%conn)        #打印新连接进来的客户端信息
            inputs.append(conn)     #将新的连接的客户端信息放入inputs队列中，以便下次通过select来检测，如果下次该socket还处于活动状态，并有数据发送，则加入队列中

            msg_quenes[conn] = queue.Queue()            #如果客户端有数据要传输，则将数据存入相应的队列中

        else:               #表示通过select监控，客户端socket是新创建的连接信息
            data = r.recv(1024)       #表示新的socket的客户端有数据发送，服务器端接收数据
            msg_quenes[r].put(data)         #将从socket客户端接收到的数据存到socket对应的队列中
            outputs.append(r)               #并将此socket信息存放在outputs中，outputs在select下一次监控的时候，如果outputs有数据，则发挥给writable，这样做为了服务器端
                                            #发送数据给客户端方便

    for w in writeable:             #此刻表示socket连接通过select监控，也在writeable列表中，则表示需要返回给客户端数据
        data_to_client = msg_quenes[w].get()
        w.send(data_to_client)      #返回给客户端数据
        outputs.remove(w)           #一次处理完socket客户端请求，则在outputs队列中删除，select下次监控不会监控老的socket连接，则不会返回数据给老连接
        print("conn %s send data to client %s "%(w,data_to_client))







