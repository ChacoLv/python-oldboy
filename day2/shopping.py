# -*- coding:utf-8 -*-
# LC
'''
goods=[[1,'iphone',5800],[2,'Mac Pro',12000],[3,'apple',30],[4,'egg',5],[5,'pig',2000]]         #商品列表
salary = input('Please input your salary:')                                                       #输入薪资
shopping_cart = []                                           #购物车列表
shopping_money=[]                                           #消费金额列表
salary=int(salary)
balance=int(salary)                                         #消费余额，未开始消费等于薪资
shopping_total_money=0
while True:
    for i in goods:                                         #打印商品清单
        print(i)
    select = input("Please input your select,or input 'q' to quit:")        #输入购买清单选项，按"q"退出
    if select=="q":
        if balance==salary:                                                         #判断是否购买了东西
            print("Do not buy any thing")
            break
        else:
            print("You have been bought below:")
            for k in shopping_cart:
                print(k)
            print("Total Comsume:",shopping_total_money)
            break
    else:
        select_sequence = int(select)
        goods_max_sequence = int(goods[-1][0])
        if select_sequence>goods_max_sequence:                                        #如果输入序列号大于商品序列号，提示输入错误
            print("------------Warning-------------")
            print("Your selected is not correctly,please retry")
            print("------------Warning-------------")
        else:
            goods_price = int(goods[select_sequence - 1][2])
            if goods_price<=balance:                                                #如果余额大于购买商品的金额，则加入购物车
                shopping_cart.append(goods[select_sequence-1])
                shopping_money.append(goods_price)                              #消费金额加入消费金额列表
                shopping_total_money = sum(shopping_money)                      #计算商品总金额
                shopping_total_money=int(shopping_total_money)
                balance = salary - shopping_total_money                         #余额计算
            else:
                print('You have not enough money!')                 #余额不足，提示购买清单
                for k in shopping_cart:
                    print(k)
                print("Total Comsume:", shopping_total_money)
                break

'''

product_list = [["apple",180],["pig",1800],["rice",5],["bike",500]]
for item in product_list:
    print(product_list.index(item),item)
print("\033[32;1m Please choice what to buy\033[0m")