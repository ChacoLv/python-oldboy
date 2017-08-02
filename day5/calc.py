# -*- coding:utf-8 -*-
# LC

import re

def search(str):
    new_str = re.search(r'\([^()]+\)',str).group()

def mul_div(str1):
    exit_flag = False
    str1 = re.sub(r"\s","",str1)
    while not exit_flag:
            if "*" in str1:
                equation = re.search(r"(([\d|.]+[e-|\d]*)\*([\d|.]+[e\-|\d]*))",str1).group()
                num1 = float(equation.split("*")[0])
                num2 = float(equation.split("*")[1])
                res = num1*num2
                res = str(res)
                str1 = re.sub(r"(([\d|.]+[e-|\d]*)\*([\d|.]+[e-|\d]*))",res,str1,count=1)
                print(str1)
            elif "/" in str1:
                equation = re.search(r"(([\d|.]+[e-|\d]*)/([\d|.]+[e-|\d]*))",str1).group()
                num1 = float(equation.split("/")[0])
                num2 = float(equation.split("/")[1])
                res = num1/num2
                res = str(res)
                str1 = re.sub(r"(([\d|.]+[e-|\d]*)/([\d|.]+[e-|\d]*))",res,str1,count=1)
                print(str1)
            else:
                exit_flag  = True
                return str1

def add_sub(str1):
    #要求输入的字符串必须为不带（）的数值加减，如'-3.1-2.3+3.5-1.2+3-9-9.555+6.555'
    #逐步取字符串的数字，取两个数字，进行相加，如果有负数or减法，则均为负数，使用加法做运算
    #取出第一个数字，则将数字从字符串中取出
    #如果能够取第二个数字，则将两数相加的结果替代
    #取至最后，替换完后则返回计算结果
    exit_flag = False
    str1 = re.sub(r"\s","",str1)
    while not exit_flag:
        if str1.startswith("-"):
            num1 = re.match(r"(-[\d|.]+[e-|\d]*)",str1).group()
            str1 = re.sub(r"(-[\d|.]+[e-|\d]*)","",str1,count=1)
            if str1.startswith("-"):
                num2 = re.match(r"(-[\d|.]+[e-|\d]*)",str1).group()
                res = float(num1) + float(num2)
                res = str(res)
                str1 = re.sub(r"(-[\d|.]+[e-|\d]*)",res,str1,count=1)
            elif str1.startswith("+"):
                num2 = re.search(r"([\d|.]+[e-|\d]*)",str1).group()
                res = float(num1) + float(num2)
                res = str(res)
                str1 = re.sub(r"(\+[\d|.]+[e-|\d]*)",res,str1,count=1)
            else:
                res = float(num1)
                return res
        else:
            num1 = re.match(r"([\d|.]+[e-|\d]*)",str1).group()
            str1 = re.sub(r"([\d|.]+[e-|\d]*)","",str1,count=1)
            if str1.startswith("-"):
                num2 = re.match(r"(-[\d|.]+[e-|\d]*)",str1).group()
                res = float(num1) + float(num2)
                res = str(res)
                str1 = re.sub(r"(-[\d|.]+[e-|\d]*)",res,str1,count=1)
            elif str1.startswith("+"):
                num2 = re.search(r"([\d|.]+[e-|\d]*)", str1).group()
                res = float(num1) + float(num2)
                res = str(res)
                str1 = re.sub(r"(\+[\d|.]+[e-|\d]*)",res,str1,count=1)
            else:
                res = float(num1)
                return res




def re_str(str1):
    while True:
        if '--' in str1:
            str1 = str1.replace("--","+")
        elif '+-' in str1:
            str1 = str1.replace("+-","-")
        elif '-+' in str1:
            str1 = str1.replace("-+","-")
        elif '++' in str1:
            str1 = str1.replace("++","+")
        else:
            return str1





str1 = '3.1-+2.3++3.5-1.2-+3-9-9.555+6.555'


print(str1)
b = re_str(str1)
print(b)

a = add_sub(b)
print(a)
