# -*- coding:utf-8 -*-
# LC

import sys
print(sys.getdefaultencoding())

s = "杭州"                    #python 3中文件内的字符串默认是unicode
print(s,type(s))
print(s)
s = s.encode("gbk")         #将unicode编码成gbk
print(s,"=========")
s_to_unicode = s.decode("gbk")  #将编码由gbk转换成unicode，这个意识是告知s原本是gbk的编码需要转换成unicode
print(s_to_unicode)

unicode_to_utf8 = s_to_unicode.encode("utf-8")      #将原本是unicode的转换成utf-8
print(unicode_to_utf8)
utf8_to_gb2312 = unicode_to_utf8.decode("utf-8").encode("gb2312") #将原本是utf-8的转换成gb2312,中间需要通过先decode转换成unicode，再将unicode通过encode转换成gb2312
print(utf8_to_gb2312)
