# -*- coding:utf-8 -*-
# LC
#sys模块

import sys
print(sys.path)     #打印环境变量
print(sys.argv)     #打印相对路径,在python命令下执行



import os
#os.system("dir")        #直接打印输出，不会保存结果
os.popen("dir")   #执行命令，并存储结果（存储的结果是在内存上）
cmd_res = os.popen("dir").read()    #执行命令，并存储结果至内存，通过read模块读取内存数据，并赋值给cmd_res
print("--->",cmd_res)

os.mkdir("new_dir")     #创建目录
os.rmdir("new_dir")     #删除目录

