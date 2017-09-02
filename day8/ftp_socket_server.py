import socket,os,hashlib

server = socket.socket()
server.bind(("localhost",9998))
server.listen()

while True:
    conn,addr = server.accept()
    print("client:%s is connected",conn)
    while True:
        m = hashlib.md5()
        cmd = conn.recv(1024)
        filename = cmd.decode().split()[1]  #获取需要传的文件名
        if os.path.isfile(filename):        #判断要传输的文件的大小
            f = open(filename,"rb")
            file_size = os.stat(filename).st_size
            conn.send(str(file_size).encode())  #发送要发送的文件大小
            conn.recv(1024)
            for line in f:
                m.update(line)              #发送文件，每次发送进行hash
                conn.send(line)
            f.close()
            print("file is send over ! ")
            print("file md5 is:",m.hexdigest())
            conn.send(m.hexdigest().encode())