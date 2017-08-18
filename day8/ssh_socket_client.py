import socket
client = socket.socket()
client.connect(("localhost",9998))


while True:
    data_size = 0
    data = ""
    cmd = input(">>:").strip()
    if len(cmd) == 0: continue
    client.send(cmd.encode("utf-8"))
    data_len = client.recv(1024).decode()
    client.send("准备好了，可以发包了".encode("utf-8"))
    print("server send len is :%s"%(data_len))
    while data_size<int(data_len):

        data_recv = client.recv(1024)
        data_size += len(data_recv.decode())
        data += data_recv.decode()
    print("client received size is %s"%(data_size))




    print("received data",data)