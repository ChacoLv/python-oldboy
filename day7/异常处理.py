# -*- coding:utf-8 -*-
# LC
names = ["Alex","Jack"]
dict = {}

try:
    names[3]
except IndexError as e:         #抓具体的错误类型
    print("ERROR !!!",e)

try:
    names[3]
except Exception as e:          #包含所有的错误类型，不建议使用，建议使用在最后抓未知错误
    print("ERROR !!!",e)



try:
    dict["age"]
except KeyError as e:         #抓具体的错误类型
    print("ERROR !!!",e)

try:
    #dict["age"]
    #names[3]
    print(names[3])
except (IndexError,KeyError) as e:  #抓取两个错误中的任意一个，代码谁先出错则执行谁
    print("ERROR",e)
else:                           #没有错的时候执行
    print("all is well")

finally:                        #不管有没有错，都执行
    print("不管有你没有错，都执行")


class TestException(Exception):     #自定义异常
    def __init__(self,msg):
        self.msg = msg

try:
    raise TestException('自定义异常')
except TestException as e:
    print(e)