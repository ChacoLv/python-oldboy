import socket,json,os
import hashlib

class FtpClient(object):
    def __init__(self):
        self.client = socket.socket()
        self.user_data = {
            "account_id": None,
            "is_authenticated": None,
            "account_data": None
        }

    def connect(self,ip,port):
        self.client.connect((ip,port))      #连接服务器

    def user_login(self):             #用户登陆程序
        retry_count = 0
        while self.user_data["is_authenticated"] is not True and retry_count < 3:
            username = input("username:").strip()
            password = input("password:").strip()
            hash_pwd = hashlib.md5(password.encode()).hexdigest()
            user_info = {
                "username":username,
                "password":hash_pwd
            }
            self.client.send(json.dumps(user_info).encode())        #发送用户认证信息，通过json格式发送
            data = self.client.recv(1024).decode()                   #接收服务器端信息，限定为认证成功后，服务器传递过来的用户信息
            print(data)
            if data.startswith("40"):                   #判断是否是错误信息，设定了几种客户端输入错误的情况，即4XX，包含密码错误，用户不存在错误
                print(data)
            else:                                       #如果不是错误信息，则为正确信息，服务器端将发送用户数据过来，接收用户数据
                acccount_data = json.loads(data)
                self.user_data["is_authenticated"] = True
                self.user_data["account_id"] = username
                self.user_data["account_data"] = acccount_data
            retry_count += 1

    def interactive(self):
        if self.user_data["is_authenticated"]:
            while True:
                cmd = input(">>").strip()       #输入要执行的命令
                if len(cmd) == 0:continue
                cmd_str = cmd.split()[0]
                if hasattr(self,"cmd_%s"%cmd_str):  #判断输入的指令是否有方法处理
                    func = getattr(self,"cmd_%s"%cmd_str)
                    func(cmd)
                else:
                    self.help()
        else:
            print("user authentication failed...")

    def cmd_put(self,*args):
        cmd_split = args[0].split()
        if len(cmd_split) > 1:
            filename = cmd_split[1]
            if os.path.isfile(filename):
                filesize = os.stat(filename).st_size
                msg = {
                    "action":"put",
                    "filename":filename,
                    "size":filesize
                }
                self.client.send(json.dumps(msg).encode("utf-8"))
                #防止粘包，需等待服务器发送确认
                server_return = self.client.recv(1024).decode()      #将服务器返回的信息记录下来，作为下一步判断的依据
                print("server return information is %s"%server_return)
                if server_return.find("200") >= 0:     #如果服务器返回的信息中包含200，则继续往下
                    f = open(filename,"rb")
                    send_size = 0
                    for line in f:
                        send_size += len(line)
                        self.client.send(line)
                        upload_percent = round(float(send_size/filesize)*100,2)
                        print("upload progress：",upload_percent)
                    else:
                        print(filename,"has been upload")
                        f.close()
            else:
                print("input filename is not exist...")

        else:
            print("invalid input command,no filename input...")

    def cmd_get(self):
        pass

    def help(self):
        '''定义ftp 客户端可执行指令'''
        msg ='''
        ftp useful command list:
        ls
        pwd
        cd dir
        put filename
        get filename
        '''
        print(msg)



ftp = FtpClient()
ftp.connect("localhost",9999)
ftp.user_login()
ftp.interactive()