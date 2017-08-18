import socket

client = socket.socket()    #声明socket类型，同时生成socket连接对象
client.connect(('localhost',6969))

while True:
    msg = input(">>:").strip()
    if not msg:continue             #判断输入端是否为空，如果为空，则继续输入
    print("type!!",type(msg))
    client.send(msg.encode(encoding="utf-8"))
    print(msg.encode(encoding="utf-8"))
    data = client.recv(1024)
    print("recv:",data.decode())

