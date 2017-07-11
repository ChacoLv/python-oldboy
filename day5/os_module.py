# -*- coding:utf-8 -*-
# LC
'''
import os
os.getcwd()                                      #获取当前工作目录，即当前python脚本工作的目录路径
os.chdir("dirname")                             #改变当前脚本工作目录；相当于shell下cd
os.curdir                                        #返回当前目录: ('.')
os.pardir                                         #获取当前目录的父目录字符串名：('..')
os.makedirs('dirname1/dirname2')                #可生成多层递归目录
os.removedirs('dirname1')                       #若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
os.mkdir('dirname')                             #生成单级目录；相当于shell中mkdir dirname
os.rmdir('dirname')                              #删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
os.listdir('dirname')                               #列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
os.remove()                                           #删除一个文件
os.rename("oldname","newname")                      #重命名文件/目录
os.stat('path/filename')                            # 获取文件/目录信息
os.sep                                              #输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
os.linesep                                          #输出当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
os.pathsep                                          #输出用于分割文件路径的字符串
os.name                                             #输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
os.system("bash command")                   #运行shell命令，直接显示
os.environ                                  #获取系统环境变量
os.path.abspath('dirname')                   #返回path规范化的绝对路径
os.path.split('dirname')                            #将path分割成目录和文件名二元组返回
os.path.dirname('dirname')                   #返回path的目录。其实就是os.path.split(path)的第一个元素
os.path.basename('dirname')                  #返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
os.path.exists('dirname')                    #如果path存在，返回True；如果path不存在，返回False
os.path.isabs('dirname')                         #如果path是绝对路径，返回True
os.path.isfile('dirname')                        #如果path是一个存在的文件，返回True。否则返回False
os.path.isdir('dirname')                             #如果path是一个存在的目录，则返回True。否则返回False
os.path.join('dirname'[, 'dirname'[, ...]])             #将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
os.path.getatime('dirname')                      #返回path所指向的文件或者目录的最后存取时间
os.path.getmtime('dirname')                          #返回path所指向的文件或者目录的最后修改时间
'''
import sys
# print(sys.argv[1])      #可以处理传递的参数
# F:\python\oldboy\day5>python os_module.py 1 2 3
# 1

# sys.argv
# F:\python\oldboy\day5>python os_module.py 1 2 3      #1,2,3是参数
# ['os_module.py', '1', '2', '3']
# import time
# for i in range(100):
#     time.sleep(0.1)
#     sys.stdout.flush()
#     sys.stdout.write('!')

# print(sys.path)
# print(sys.platform)
# sys.version