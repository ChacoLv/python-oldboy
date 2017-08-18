import socket,os,time

server = socket.socket()
server.bind(("localhost",9998))
server.listen()

while True:
    conn,addr = server.accept()
    print("client:%s is connecting",conn)
    while True:
        data = conn.recv(1024)
        print(type(data))
        if not data:
            print("client is disconnected ! ! !")
            break
        cmd_res = os.popen(data.decode()).read()
        data_len = len(cmd_res)
        print("server send size is %s"%(data_len))
        conn.send(str(data_len).encode("utf-8"))
        client_ack = conn.recv(1024).decode()
        conn.send(cmd_res.encode("utf-8"))

