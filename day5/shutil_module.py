# -*- coding:utf-8 -*-
# LC

import shutil
# f1 = open("file1",encoding="utf-8")
# f2 = open("file2","w",encoding="utf-8")
# shutil.copyfileobj(f1,f2)
# shutil.copy("file2","file3")        #复制文件和权限
# shutil.copystat("file3","file2")            #复制权限信息，但是内容不拷贝
# shutil.copyfile()                   #复制文件
# shutil.copytree()                   #递归复制，即复制整一个目录，包含内容
# shutil.rmtree()                     #递归删除，即将目录所有内容删除
# shutil.copymode()               #仅拷贝权限，内容，组，用户均不变
# shutil.move()               #移动目录
# shutil.make_archive("shutil_archive_test","zip","F:\python\oldboy\day5")    #压缩文件名，压缩类型，要压缩的文件目录

import zipfile
z = zipfile.ZipFile("day5.zip","w")
z.write("file2")
z.write("file1")

