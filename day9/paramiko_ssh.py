import paramiko

#创建ssh对象
ssh = paramiko.SSHClient()
#设置允许连接的主机不在know hosts列表里面连接
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#连接ssh主机
ssh.connect(hostname="10.210.2.39",port=22,username="root",password="Cisco@123")
#执行命令
stdin,stdout,stderr = ssh.exec_command("ifconfig | grep 'inet '")

res,err = stdout.read(),stderr.read()

result = res if res else err

#打印结果
print(result.decode())

ssh.close()
