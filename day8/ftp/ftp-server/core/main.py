import socketserver
import json
import os

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client

        while True:
            try:
                self.data = self.request.recv(1024).strip()
                cmd_dic = json.loads(self.data.decode())
                action = cmd_dic["action"]
                if hasattr(self,action):            #判断客户端传送过来的指令是否存在，如果不存在，不执行
                    func = getattr(self,action)
                    func(cmd_dic)
                else:
                    print("actcion {%s} is not exist..."%action)
                    self.request.send(b"500, command is not exist")

            except ConnectionAbortedError as e:
                print("error ",e)
                break

    def put(self,*args):
        filename = args[0]["filename"]
        filesize = args[0]["size"]
        recv_size = 0
        self.request.send(b"200 ack")       #返回给客户端，表示可以进行传输
        if os.path.isfile(filename):
            f = open(filename + ".new","wb")
        else:
            f = open(filename,"wb")
        while recv_size < filesize:
            data = self.request.recv(1024)
            f.write(data)
            recv_size += len(data)
        else:
            print("file:%s has uploaded...."%filename)
            f.close()









if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()