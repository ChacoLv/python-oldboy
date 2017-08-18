# -*- coding:utf-8 -*-
# LC


# 导入模块是将模块中所有的代码打包成一个文件，通过.来调用
import os
# 导入包的本质是运行包中的__init__文件

#导入模块中某个函数或者变量
#from test import hello      #将test模块中的hello函数导入，在本模块中可以直接调用，也可以通过as来另起名字

#模块的分类
# 1. 标准库
# 2. 开源模块
# 3. 自定义模块

#时间模块,time
import time
#时间戳
x = time.time()
time.gmtime()   #将时间戳转换成UTC时间元组
y = time.localtime()    #将时间戳转换成本地时区的时间元组
print(y)
#结构化数据，为元组的形式
y = time.mktime(y)       #将结构化数据转换成时间戳
print(y)

#格式化数据
z = time.strftime("%Y-%m-%d %H:%M:%S",y) #将结构化数据转换成格式化数据
#time.strftime("格式","结构化的时间数据（元组）")  --->将结构化时间数据转化成格式化时间数据
#time.strptime("格式化时间字符串","格式")  ----->按着给定的格式进行匹配格式化时间字符串，并转换成格式化时间数据

# >>> x = time.localtime()
# >>> print(x)
# time.struct_time(tm_year=2017, tm_mon=7, tm_mday=9, tm_hour=23, tm_min=11, tm_se
# c=32, tm_wday=6, tm_yday=190, tm_isdst=0)
# >>> time.strftime("%Y-%m-%d %H:%M:%S",x)        #即%Y去匹配tm_year,%m匹配tm_mon，无须注意顺序
# '2017-07-09 23:11:32'
# >>>
# >>> time.strptime('2017-07-09 23:11:32',"%Y-%m-%d %H:%M:%S")    %Y 匹配2017,必须注意顺序
# time.struct_time(tm_year=2017, tm_mon=7, tm_mday=9, tm_hour=23, tm_min=11, tm_se
# c=32, tm_wday=6, tm_yday=190, tm_isdst=-1)
#
# time.ctime(x)   #将时间戳数据转换成特定格式
# >>> time.ctime(x)
# 'Mon Jul 10 19:26:16 2017'
# >>> time.asctime(y) #将结构化数据转换成特定格式
# 'Mon Jul 10 19:26:45 2017'

import datetime
print(datetime.datetime.now()) #返回 2016-08-19 12:47:03.941925
print(datetime.date.fromtimestamp(time.time()) )  # 时间戳直接转成日期格式 2016-08-19
print(datetime.datetime.now() )
print(datetime.datetime.now() + datetime.timedelta(3)) #当前时间+3天
print(datetime.datetime.now() + datetime.timedelta(-3)) #当前时间-3天
print(datetime.datetime.now() + datetime.timedelta(hours=3)) #当前时间+3小时
print(datetime.datetime.now() + datetime.timedelta(minutes=30)) #当前时间+30分
c_time  = datetime.datetime.now()
print(c_time.replace(minute=3,hour=2)) #时间替换

























