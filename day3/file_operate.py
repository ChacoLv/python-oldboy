# -*- coding:utf-8 -*-
# LC

f = open("lyrics","r",encoding="utf-8")           #以utf-8的编码方式打开文件，文件句柄
data = f.read()         #读取文件内容

f = open("lyrics","w",encoding="utf-8")         #以写的方式打开，且为创建一个文件
f.write("今天上班\n")
f.write("明天下班\n")

f = open("lyrics","a",encoding="utf-8")         #以追加的方式写入，但不能够读取
f.write("追加写入\n")

f = open("lyrics","r+",encoding="utf-8")    #以读写的方式打开，即可读，也可写（追加），但写是从文件的最后开始写
print(f.readline())
print(f.readline())
f.write("===================")
f.close()

f = open("lyrics","w+",encoding="utf-8")    #以写读的方式打开文件，即先创建一个文件，然后可读写，读可以实现位置移动，写是否根据光标需要看版本
f.write("+++---------------------+++\n")
f.write("+++---------------------+++\n")
f.write("+++---------------------+++\n")
print(f.tell())
f.seek(30)
print(f.tell())
f.write("************")

f = open("lyrics","a+",encoding="utf-8")    #追加读写，原本a是只可追加，不可读，现是可读写的,读默认是在末尾，如果需要从头读，则需要seek(0a)
for line in f:
    print(line)

f = open("lyrics","rb")         #以二进制模式读
print(f.readline())
f = open("lyrics","wb")         #以二进制模式写入
f.write("hello\n".encode())     #默认是写入字符串，如果是二进制，则需要将字符串转换为二进制格式

f = open("lyrics","r",encoding="utf-8")
print(f.readline())                           #读取文件中的一行
print(f.readlines())                            #读取整个文件，并将每行作为列表的一个元素存储,只适合读取小文件，大文件会撑爆内存

f = open("lyrics","r",encoding="utf-8")
for index,line in enumerate(f.readlines()):                  #将文件读取成一个列表，每行是列表的元素，通过赋值line循环
    if index == 9:
        print("==============================")
    print(line.strip())


f = open("lyrics","r",encoding="utf-8")
for line in f:                              #将文件中的每一行赋值给line，line为字符串类型
    print(line.strip())

print(f.read(12))               #读取12个字符
print(f.readline())
print(f.tell())             #告知现有光标位置
f.seek(0)               #表示回到文件某个位置

print(f.encoding)       #表示打开文件的编码方式
print(f.name)           #打印文件名
print(f.seekable())     #判读文件是否可移动，如tty是不可以移动的
print(f.readable())     #判断文件是否可读
print(f.writable())     #判断文件是否可写
print(f.flush())        #强制刷新，默认是内存将数据存在缓存中，然后缓存聚集成一块后再统一刷到硬盘
f.closed                #判读是否关闭

f = open("lyrics","a",encoding="utf-8")
f.truncate(20)      #表示从文件头截断20个字符，seek无效，都是从头开始截断

#打印进度条
import sys,time
for i in range(100):                    #打印进度条
    sys.stdout.write("!")               #系统标准输出，不会换行
    sys.stdout.flush()                  #每打印一个，立即刷新，即从内存中立即刷新
    time.sleep(0.1)                     #每个延迟0.1秒

