# -*- coding:utf-8 -*-
# LC
import random
# print(random.randint(1,9))
# print(random.random())
#
# print(random.randrange(2,10,4))
# print(random.sample('chenglv',2))
# print(random.randrange(0,99,2))
# print(random.uniform(1,10))

checkcode = ""
for i in range(4):
    x = random.randint(0, 9)
    y = random.choice("adbcdefglikopnm")
    if i == random.randint(0,3):
        tmp = x
    else:
        tmp = y
    checkcode += str(tmp)

print(checkcode)