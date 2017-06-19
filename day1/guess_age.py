# -*- coding:utf-8 -*-
# LC
import getpass
'''
username = "Lv Cheng"
age = 18
count = 0

while count < 3:
    _age = int(input("age of %s:"%username))
    if _age == age:
        print("You got it")
        break
    elif _age < age:
        print("bigger")
    else:
        print("smaller")
    count +=1
    if count == 3:
        continue_guess = input("Do you want to continue to guess?")     #看是否需要继续猜
        if continue_guess != "n":
            count = 0

#else:
 #   print("you have tried too many times.")         #当次数超过三次，退出


for i in range(3):
    _age = int(input("age of %s:" % username))
    if _age == age:
        print("You got it")
        break
    elif _age < age:
        print("bigger")
    else:
        print("smaller")
    count += 1
else:
    print("you have tried too many times.")
'''
'''
for i in range(0,10):
    if i<5:
        print(i)
    else:
        print("hello")
        continue

#打印IP地址段
for i in range(255):
    for j in range(255):
        for k in range(1,255):
            print("10.%d.%d.%d"%(i,j,k))

'''

for i in range(255):
    for j in range(255):
        for k in range(1,255):
            print("10.{_i}.{_j}.{_k}".format(_i=i,_j=j,_k=k))
