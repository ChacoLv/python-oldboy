# -*- coding:gbk -*-
# LC
'''
f = open("lyrics","r",encoding="utf-8")           #��utf-8�ı��뷽ʽ���ļ����ļ����
data = f.read()         #��ȡ�ļ�����

f = open("lyrics","w",encoding="utf-8")         #��д�ķ�ʽ�򿪣���Ϊ����һ���ļ�
f.write("�����ϰ�\n")
f.write("�����°�\n")

f = open("lyrics","a",encoding="utf-8")         #��׷�ӵķ�ʽд�룬�����ܹ���ȡ
f.write("׷��д��\n")

f = open("lyrics","r+",encoding="utf-8")    #�Զ�д�ķ�ʽ�򿪣����ɶ���Ҳ��д��׷�ӣ�����д�Ǵ��ļ������ʼд
print(f.readline())
print(f.readline())
f.write("===================")
f.close()

f = open("lyrics","w+",encoding="utf-8")    #��д���ķ�ʽ���ļ������ȴ���һ���ļ���Ȼ��ɶ�д��������ʵ��λ���ƶ���д�Ƿ���ݹ����Ҫ���汾
f.write("+++---------------------+++\n")
f.write("+++---------------------+++\n")
f.write("+++---------------------+++\n")
print(f.tell())
f.seek(30)
print(f.tell())
f.write("************")

f = open("lyrics","a+",encoding="utf-8")    #׷�Ӷ�д��ԭ��a��ֻ��׷�ӣ����ɶ������ǿɶ�д��,��Ĭ������ĩβ�������Ҫ��ͷ��������Ҫseek(0a)
for line in f:
    print(line)

f = open("lyrics","rb")         #�Զ�����ģʽ��
print(f.readline())
f = open("lyrics","wb")         #�Զ�����ģʽд��
f.write("hello\n".encode())     #Ĭ����д���ַ���������Ƕ����ƣ�����Ҫ���ַ���ת��Ϊ�����Ƹ�ʽ

f = open("lyrics","r",encoding="utf-8")
print(f.readline())                           #��ȡ�ļ��е�һ��
print(f.readlines())                            #��ȡ�����ļ�������ÿ����Ϊ�б��һ��Ԫ�ش洢,ֻ�ʺ϶�ȡС�ļ������ļ���ű��ڴ�

f = open("lyrics","r",encoding="utf-8")
for index,line in enumerate(f.readlines()):                  #���ļ���ȡ��һ���б�ÿ�����б��Ԫ�أ�ͨ����ֵlineѭ��
    if index == 9:
        print("==============================")
    print(line.strip())


f = open("lyrics","r",encoding="utf-8")
for line in f:                              #���ļ��е�ÿһ�и�ֵ��line��lineΪ�ַ�������
    print(line.strip())

print(f.read(12))               #��ȡ12���ַ�
print(f.readline())
print(f.tell())             #��֪���й��λ��
f.seek(0)               #��ʾ�ص��ļ�ĳ��λ��

print(f.encoding)       #��ʾ���ļ��ı��뷽ʽ
print(f.name)           #��ӡ�ļ���
print(f.seekable())     #�ж��ļ��Ƿ���ƶ�����tty�ǲ������ƶ���
print(f.readable())     #�ж��ļ��Ƿ�ɶ�
print(f.writable())     #�ж��ļ��Ƿ��д
print(f.flush())        #ǿ��ˢ�£�Ĭ�����ڴ潫���ݴ��ڻ����У�Ȼ�󻺴�ۼ���һ�����ͳһˢ��Ӳ��
f.closed                #�ж��Ƿ�ر�

f = open("lyrics","a",encoding="utf-8")
f.truncate(20)      #��ʾ���ļ�ͷ�ض�20���ַ���seek��Ч�����Ǵ�ͷ��ʼ�ض�

#��ӡ������
import sys,time
for i in range(100):                    #��ӡ������
    sys.stdout.write("!")               #ϵͳ��׼��������ỻ��
    sys.stdout.flush()                  #ÿ��ӡһ��������ˢ�£������ڴ�������ˢ��
    time.sleep(0.1)                     #ÿ���ӳ�0.1��
'''


#�ļ��޸�
'''
for line in f_read:
    if line == "���յ����������\n":
        line = "hellooooooooooo\n"
    f_write.write(line)
f_read.close()
f_write.close()

#�ļ��޸ģ�sed���滻
import sys
f_read = open("lyrics","r",encoding="utf-8")            #�ļ��޸ĵ�˼·�������޸ĺõ��ļ���������һ���ļ���
f_write = open("file1","w",encoding="utf-8")
find_str = sys.argv[1]                              #��ʾ����ִ��ʱ�����ĵ�һ������
replace_str = sys.argv[2]                           #��ʾ����ִ��ʱ�������ĵڶ�������
for line in f_read:
    if find_str in line:
        line = line.replace(find_str,replace_str)   #�ַ��������滻
    f_write.write(line)

f_read.close()
f_write.close()

# ʹ��with�򿪣�����Ҫ�رգ�withִ���꣬�ļ��ر�
with open("lyrics","r") as file_1,open("file1","w") as file_2:      #ͬʱ�򿪶���ļ�
    print(file_1)
'''




