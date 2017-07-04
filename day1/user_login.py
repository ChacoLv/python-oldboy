# -*- coding:utf-8 -*-
# LC
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
username = input("please input your username:")         #输入用户名
#检查用户名是否被锁住
lock_read = open("lock_file.txt","r")
for lock in lock_read:
    lock_user = lock.strip()            #取出lock文件里面的用户信息
    if username == lock_user:
        print("You have been locked!")
        break
    else:
        continue
lock_read.close()                   #读取完毕

if username != lock_user:
    password = input("please input your password:")         #如果用户没有再lock文件中，则输入密码
    with  open("account_file.txt") as user_info:            #打开用户账号文件
        for account in user_info:                               #查看输入的用户是否再账号文件内
            account_user = account.strip().split(" ")[0]
            account_pass = account.strip().split(" ")[1]
            if username == account_user:                        #如果输入的用户名在用户文件中存在
                if password == account_pass:
                    print("welcome to login")               #密码正确，则判断登录成功
                    break
                else:
                    print("wrong password!")                #否则密码错误，重新输入密码，即可用再输入两次
                    for count in range(0,2):
                        count = count + 1
                        password = input("please input your password:")
                        if password == account_pass:
                            print("welcome to login")          #如果再次输入的密码正确，则跳出
                            break
                        else:
                            print("wrong password")
                    if count == 2:                              #如果三次输错，则写入lock文件中，采用追加写入的方式
                        lock_write = open("lock_file.txt","a+")
                        lock_write.write("\n")
                        lock_write.write(username)
                        lock_write.close()
        if username!=account_user:                                     #如果账号文件内没有此账号，则提出没有此用户信息
            print("No this user")




















