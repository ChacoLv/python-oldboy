import socket,hashlib
client = socket.socket()
client.connect(("localhost",9998))


while True:
    recv_size = 0
    cmd = input(">>:").strip()
    if len(cmd) == 0: continue
    if cmd.startswith("get"):
        m = hashlib.md5()
        filename = cmd.split()[1]
        client.send(cmd.encode())
        file_size = int(client.recv(1024).decode()) #接收服务器端发送过来端文件大小，用于判断
        client.send(b"begin to receive ! ")         #确认可以服务器端可以发送数据，防止粘包
        f = open(filename + ".new", "wb")           #创建文件，并以二进制方式写入
        while recv_size < file_size:
            if file_size - recv_size > 1024:        #在循环汇中将文件传输完成，防止粘包
                size = 1024
            else:
                size = file_size - recv_size
            data_recv = client.recv(size)           #开始收集文件内容
            recv_size += len(data_recv)
            m.update(data_recv)                     #对每次接收的数据进行hash
            f.write(data_recv)                      #将接收数据写入文件
            print(recv_size,file_size)
        else:
            print("data receive over ! ")
            print("receive file md5:",m.hexdigest())
            recv_file_md5 = m.hexdigest()           #对接收的数据的哈希结果按着16进制表达
            server_send_md5 = client.recv(1024)     #服务器端发送的哈希值
            print("server send md5:",server_send_md5)

            f.close()
