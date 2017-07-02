# -*- coding:utf-8 -*-
# LC
'''
print(all([1,2,3,0,4]))     #all中的课迭代对象全为真则返回真
print(any([1,2,3,0]))       #any中有一个为真则返回真
print(bin(101))             #把数字转换成2进制
print(bool({}))             #判断整数是否为真，列表，元组，字典如果为空，则返回False

a = bytes("abcde",encoding="utf-8")     #字符串默认是不能够修改的
b = bytearray("abcde",encoding="utf-8")     #将原有数据变化成一个列表，并且可以改变
b[1] = 100                          #必须要赋值一个整型，为ASCII码表对应的数字
print(b)

callable([])      #判断是否为可调用对象，函数，类都是可以调用的，即是否有()调用
print(callable([]))
def hel():pass
print(callable(hel))

chr(100)        #输入数字，返回数字对应的unicode表中的字符
print("----",chr(97))

ord("i")       #输入字符，将字符对应的unicode表的数字返回
print(ord("你"))

code = "for i in range(10):print(i)"
exec(code)      #exec能够将字符串转换成可执行代码并执行

print(dir(code))   #查看一点对象具体有什么方法可以使用

print(divmod(10.2,2.2)) #查看两张相除的结果及余数

#enumerate([])         #将可迭代对象按着序列号排序
list1 = ['January','February','March','April','May','June','July','August','September','October','November','December']
print(list(enumerate(list1,start=1)))               #表示从1开始计数，将list1中的对象分配一个序号
for index,i in enumerate(list1,start=1):
    print(index,i)

#filter
res = filter(lambda n:n>5,range(10))        #结合lambda，filter将lambda中为True的返回
for i in res:
    print(i)
#map
res = map( lambda n:n*2,range(6))           #map将lambda range中所有的元素进行运算
for i in res:
    print(i)

res = [lambda i:i*2 for i in range(10)]
#reduce
import functools
rese = functools.reduce(lambda x,y:x+y,range(5))       #表示x,y默认从0,1开始，x+y结果传递给x，y每次+1，并把结果给x
print(rese)

res = functools.reduce(lambda x,y:x*y,range(1,10))
print('----',res)

#frozeset
a = frozenset([1,2,3,5,534,4,34,2])         #表示一个不可变集合，即默认集合拥有的方法将无法使用
print(a)

#globals()          #将整个程序，仅这个文件的变量按着key，value的格式，字典的方式呈现
print(globals())

#hash

#hex            #将数字转换成16进制
#oct(x)         #将数字转换成8进制
hex(152)

#id             #返回内存地址
print('---',id(1))

#locals()           #寻找局部变量中的变量，仅在局部有效

#max()              #找出最大的值
#min()

#pow
print(pow(2,4,5))            #求x的y次方，然后使用z求余

#round
print(round(1.232122322,5))              #表示保留小数点后几位

#sorted
a = {5:2,8:0,1:4,-5:7,99:11}
print(sorted(a.items()))                #将字典a变成列表，并排序，默认按着字典的key排序
# 结果：[(-5, 7), (1, 4), (5, 2), (8, 0), (99, 11)]
print(sorted(a.items(),key=lambda x:x[1]))      #按着字典value排序，使用lambda来指定转换后的列表中的第二个数字排序
# 结果：[(8, 0), (5, 2), (1, 4), (-5, 7), (99, 11)]

#zip                #将多个可迭代对象进行相互柔和,以最短的算
a = (1,2,3,4,5,6,7)
b = ('a','b','c','d','e','f')
print(len(b))
c = ('+' for i in range(len(b)))
print(c)
for i in zip(a,b,c):
    print(i)

#map                #将可迭代对象按着函数执行，即将可迭代对象的值传递给函数，并返回结果
def hel(*args):
    return args
for i in map(hel,a,b):
    print(i)
'''
__import__("decorate")

