import paramiko

transport = paramiko.Transport(("10.210.2.39",22))
transport.connect(username="root",password="Cisco@123")

sftp = paramiko.SFTPClient.from_transport(transport)

#sftp.put("/tmp/sangfordnscmp.txt","/tmp/formac")
sftp.get("/tmp/formac","/tmp/2017")

transport.close()
sftp.close()