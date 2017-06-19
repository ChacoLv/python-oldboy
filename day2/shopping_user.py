# -*- coding:utf-8 -*-
# LC
import os
product_list = []           #定义商品清单列表
product_line = []           #定义商品清单中每行的列表
user_buy_list = []          #定义用户已经购买商品列表
user_buy_product = []       #定义用户购买单个商品的列表
with open("product_list","r") as f_production:              #读取商品清单列表
    for item_production in f_production:
        product_line = item_production.rstrip().split(",")
        product_list.append(product_line)

if os.path.getsize("shopping_list") == 0:                       #判断是否为第一次消费，如果消费清单文件为空，则第一次消费
    salary = input("Please input your salary:")
    balance = int(salary)                                           #将余额定义为薪资
else:
    length = len(open("shopping_list","rU").readlines())            #如果不是第一次消费，计算消费清单文件行数，提取消费列表
    count = 0
    with open("shopping_list", "r") as f_shopping_list:
        for shopping_item in f_shopping_list:
            count +=1
            if 2 <= count <= length-2:                          #去除第一行和最后两行，将消费清单中已购买的商品提取出来
                shopping_item = shopping_item.strip().split()   #将购买的商品转换为列表，包含商品，单价，数量
                user_buy_list.append(shopping_item)             #将已经购买的商品记录至用户消费清单列表中
            elif count == length:
                shopping_item = shopping_item.strip().split()
                balance = int(shopping_item[-1])                #如果非第一次消费，则余额为消费清单文件中的余额，提取出来
while True:
    print("This is the production list".center(50, "-"))
    count = 0
    for i in product_list:
        print(count, i)
        count += 1
    user_select = input("Your balance is %d, 's' to start to shopping,'q' to quit : "%(balance))
    if user_select == 's':
        user_buy_product = []
        user_select_index = input("Please select the index of the one you want to buy:")        #输入要购买的商品
        user_select_count = input("Please input the number how many you want to buy:")          #输入要购买的商品数量
        user_select_index = int(user_select_index)
        user_select_count = int(user_select_count)
        unit_price = int(product_list[user_select_index][1])                        #要购买的商品单价
        product_price = unit_price * user_select_count                              #购买的商品金额，即单价乘以总价
        if product_price <= balance:
            user_buy_product.append(product_list[user_select_index][0])             #将购买的商品的名称插入新的单个列表中
            user_buy_product.append(product_list[user_select_index][1])             #将购买的商品的单价插入新的单个列表中
            user_buy_product.append(str(user_select_count))                         #将购买的商品的数量插入新的单个列表中
            user_buy_list.append(user_buy_product)                                  #将新购买的商品，包含名称，单价，数量插入用户购买清单中
            balance = balance - product_price                                        #将金额出去已经购买的商品金额，以免余额不足
        else:                                                                       #购买的商品和数量，余额不足
            print("\033[1;31mYour choice is out of your money!\033[0m")
            continue
    elif user_select == 'q':
        break
    else:
        print("invalid input ,try again")
        continue

#统计用户购买商品的总金额和消费余额
total_price = 0
for i in user_buy_list:
    user_buy_product_price = int(i[1]) * int(i[2])          #用户购买的单个商品的总额，即单件商品的单价乘以数量
    total_price = total_price + user_buy_product_price      #统计消费总金额
total_consumption = ["Total_Consumption:"]
balance_list = ["Your balance:"]                            #消费清单上记录余额信息
balance_list.append(balance)
total_consumption.append(total_price)
user_buy_list.append(total_consumption)                     #将总消费金额信息插入用户消费清单中
user_buy_list.append(balance_list)                          #将余额信息插入用户消费清单中

#将用户购买的商品写入消费清单文件中，并记录总价和余额
with open("shopping_list","w") as f_buy:
    f_buy.writelines("product".center(15,"-")+"price".center(15,"-")+"count".center(15,"-")+"\n")
    for i in user_buy_list:
        if len(i) == 3:                     #将商品写入
            f_buy.writelines(str(i[0]).center(15," ")+str(i[1]).center(15," ")+str(i[2]).center(15," ")+"\n")
        else:                               #将余额和消费总额写入
            f_buy.writelines(str(i[0]).ljust(30, " ") + str(i[1]).center(15, " ") + "\n")

#打印最终购买清单
print("This is your purchase list".center(45,"-"))
with open("shopping_list","r") as f_read:
    for i in f_read:
        print(i.strip("\n"))