import socketserver
import json
import os,sys
import hashlib

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core import db_handler
from core import home_dir_handler




class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    def acc_auth(self):
        while True:
            data = self.request.recv(1024)          #接收客户端传递过来的用户认证数据
            user_info = json.loads(data.decode())
            username = user_info["username"]        #客户端传递过来的用户名
            hash_pass = user_info["password"]       #客户端传递过来的用户密码，已被md5 hash
            db_path = db_handler.db_handler()        #数据文件
            account_file = "%s/%s.json"%(db_path,username)
            if os.path.isfile(account_file):
                with open(account_file,"r") as f:
                    account_info = json.load(f)
                    password = account_info["password"]
                    h_pass = hashlib.md5(password.encode()).hexdigest()  #服务器端根据客户端提供的账号，查询密码，并进行hash
                    if hash_pass == h_pass:
                        response = "200 ack"                #认证成功，设置回应代码
                    else:
                        response = "401 password error,please retry"     #认证失败，密码错误
            else:
                response = "402 user does not exist,please retry"        #认证失败，账号不存在
            if response.startswith("200"):                          #如果认证成功，则发送用户账号信息给客户端，客户端可以查看账号信息
                user_home_dir = home_dir_handler.home_dir_handler(username)         #认证成功后，获取用户ftp家目录
                account_info["current_dir"] = user_home_dir                         #修改用户库中当前目录信息
                dir_list = os.listdir(user_home_dir)                              #获取用户当前目录文件清单
                account_info["dir_list"] = []
                for i in dir_list:
                    account_info["dir_list"].append(i)                           #将用户目录清单写入用户信息中
                self.request.send(json.dumps(account_info).encode())
                with open(account_file,"w") as f:
                    f.write(json.dumps(account_info))
                return True
            else:                                                      #如果认证失败，则发送错误代码给客户端，客户端接收并查看
                self.request.send(response.encode())
                return False


    def handle(self):
        # self.request is the TCP socket connected to the client
        if self.acc_auth():         #用户认证，如果成功，则进入下一步
            while True:
                try:
                    self.data = self.request.recv(1024).strip()     #接收客户端传过来的指令
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
        else:
            print("user authentication failed...")


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