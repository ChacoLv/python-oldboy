import socket
import os

server = socket.socket()

server.bind(('localhost',6969))
server.listen()

print("client is connecting!")

while True:                     #连接多个连接，但需要一个连接断开后，然后再进入下一个连接
    conn,addr = server.accept() #客户端进来了。
    #conn是客户端连过来，服务器端为其生成端一个连接实例，addr为于服务器连接但客户端地址信息（包含IP地址和端口号）
    print('''
        conn:%s
        addr:%s
    '''%(conn,addr))

    print("client is connected!")

    while True:             #同一个客户端连接，多次输入
        data = conn.recv(1024)
        print("type!!",type(data))
        if len(data)==0:break
        print("data is receive:",data)
        data = data.decode()
        print("new type",type(data),data)
        res = os.popen(data).read()
        conn.send(res)

server.close()