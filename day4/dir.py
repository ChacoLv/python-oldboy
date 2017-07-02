# -*- coding:utf-8 -*-
# LC
import os
print(__file__)             #__file__打印相对路径
print(os.path.abspath(__file__))        #得到该程序的绝对路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)

