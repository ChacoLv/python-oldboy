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
                equation = re.search(r"([\d|.]+\*[\d|.]+)",str1).group()
                num1 = float(equation.split("*")[0])
                num2 = float(equation.split("*")[1])
                res = num1*num2
                res = str(res)
                str1 = re.sub(r"([\d|.]+\*[\d|.]+)",res,str1,count=1)
                print(str1)
            elif "/" in str1:
                equation = re.search(r"([\d|.]+/[\d|.]+)",str1).group()
                num1 = float(equation.split("/")[0])
                num2 = float(equation.split("/")[1])
                res = num1/num2
                res = str(res)
                str1 = re.sub(r"([\d|.]+/[\d|.]+)",res,str1,count=1)
                print(str1)
            elif "+" in str1:
                equation = re.search(r"([\d|.]+\+[\d|.]+)",str1).group()
                num1 = float(equation.split("+")[0])
                num2 = float(equation.split("+")[1])
                res = num1+num2
                res = str(res)
                str1 = re.sub(r"([\d|.]+\+[\d|.]+)",res,str1,count=1)
                print(str1)
            # elif "-" in str1:
            #     if re.search(r"e-",str1):
            #         continue
            #     else:
            #         equation = re.search(r"([\d|.]+-[\d|.]+)",str1).group()
            #         num1 = float(equation.split("-")[0])
            #         num2 = float(equation.split("-")[1])
            #         res = num1-num2
            #         res = str(res)
            #         str1 = re.sub(r"([\d|.]+-[\d|.]+)",res,str1,count=1)
            #         print(str1)
            else:
                exit_flag = True




    return str


a = mul_div("(9-2*5/3 + 7/3*99/4*2998 +10 * 568/14 )")


