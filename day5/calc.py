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
    exit_flag = False
    str1 = re.sub(r"\s","",str1)
    while not exit_flag:
        if str1.startswith("-"):
            num1 = re.match(r"(-[\d|.]*)",str1).group()
            str1 = re.sub(r"(-[\d|.]*)","",str1,count=1)
            if str1.startswith("-"):
                num2 = re.match(r"(-[\d|.]*)",str1).group()
                res = float(num1) + float(num2)
                res = str(res)
                str1 = re.sub(r"(-[\d|.]*)",res,str1,count=1)
                print(str1)
            elif str1.startswith("+"):
                num2 = re.search(r"([\d|.]+)",str1).group()
                res = float(num1) + float(num2)
                res = str(res)
                str1 = re.sub(r"(\+[\d|.]*)",res,str1,count=1)
            else:
                res = float(num1)
        else:
            num1 = re.match(r"([\d|.]*)",str1).group()
            str1 = re.sub(r"([\d|.]*)","",str1,count=1)
            if str1.startswith("-"):
                num2 = re.match(r"(-[\d|.]*)",str1).group()
                res = float(num1) + float(num2)
                res = str(res)
                str1 = re.sub(r"(-[\d|.]*)",res,str1,count=1)
            elif str1.startswith("+"):
                num2 = re.search(r"([\d|.]+)", str1).group()
                res = float(num1) + float(num2)
                res = str(res)
                str1 = re.sub(r"(\+[\d|.]*)",res,str1,count=1)
            else:
                res = float(num1)


a = add_sub("-3.1-2.3+3.5-1.2")
print(a)


