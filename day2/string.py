# -*- coding:utf-8 -*-
# LC
string = "actions speak"
print(string.capitalize())      #首字母大写
print(string.split())                           #将字符串划分出列表，默认是空格，可以定义分隔符

string = "hello {name} old {age}"
print(string.format(name="chaco",age=19))       #{}结合format输出相应字符串
#hello chaco old 19

print(string.count("a"))        #统计字符串中"a"的数量
print(string.center(50,"-"))    #表示打印字符串多长，不够的用"-"替代
print(string.isdigit())             #判读是否为整数
print(string.isidentifier())        #判断是否为一个合法的变量名


string = "actions\t speak"
print(string.expandtabs(tabsize=30))    #表示tab间隔长度
#actions                        speak

string = "better late than never"
print(string.find("late"))      #查找子字符串出现的位置
#print(string.index("old"))                      #输出子字符串的位置

string = "Better LBate Than NeverB"

print("+".join(["1","2","3"]))          #将列表整合
#1+2+3

print(string.ljust(50,"-"))         #靠左对齐，并打印相应长度，不够以"-"补齐
#Better Late Than Never----------------------------
print(string.rjust(50,"+"))
#++++++++++++++++++++++++++++Better Late Than Never

print(string.lower())               #大写变小写
print(string.upper())               #小写变大写

print(string.lstrip("B"))           #从最左边去除第一个子字符串,子字符串默认为空格和回车
print(string.rstrip("B"))           #从最右边去除第一个子字符串，子字符串默认为空格和回车

string = "Hello LvCheng"
tran = str.maketrans("ABCDEFG","1234567")       #表示两个子字符串对应关系
print(string.translate(tran))                       #string中按着子字符串对应关系做转化

print(string.replace("e","E",1))              #表示将字符串中的某个子字符串替换成另一个子字符串，并且限制次数，默认替换所有
string = "hello lvCheng"
print(string.rfind("e"))                        #从左往右，找到最右的子字符串的位置
print(string.splitlines())                      #按着换行划出列表
print(string.swapcase())                        #将大写换小写，小写换大写

string = "hello lVCheng"
print(string.title())                           #将字符串变成title
#Hello Lvcheng
print(string.zfill(40))                         #设置长度，不够以"0"补充
#000000000000000000000000000Hello LvCheng

print(string.encode())          #将字符串变成二进制
print(string.endswith("ds"))    #判断以什么结尾，返回True或者Flase
print(string.isalnum())             #判读是否为只含有字母和数字的字符串
print(string.isalpha())             #判读是否只为字母，包含大小写
print(string.islower())             #判读是否为全小写
print(string.isprintable())         #判断是否可以打印，vty之类是不可打印的
print(string.isspace())             #判断是否为空格
print(string.istitle())             #判断是否为title
print(string.isupper())             #判断是否为全大写