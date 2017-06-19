# -*- coding:utf-8 -*-
# LC
product_list = []
product_line = []
count = 0

with open("product_list","r") as f:                     #打开商家货品清单文件
    for item in f:
        product_line = item.rstrip().split(",")            #将每行赋值给成一个列表，以“，”区分
        product_list.append(product_line)                   #将每行的列表加入product_list列表中

print("This is your production".center(50,"-"))         #打印列表
for i in product_list:
    print(count,i)
    count+=1

#提供增加商品，修改商品价格，删除商品功能
while True:
    select = input("Please input you selection,'a' to add,'m' to modified the price,'d' to Delete,'q' to quit :")
    count = 0
    if select == 'a':
        add_product = input("Please input new product name:")
        add_price = input("Please input new product price:")
        new_product = [add_product,add_price]                       #将新添加的商品赋值成列表
        product_list.append(new_product)                            #向产品清单列表中插入新添加的商品
        with open("product_list","a") as f_add:                 #将添加的商品写入文件中，以追加的方式
            f_add.writelines(product_list[-1][0]+","+product_list[-1][1]+"\n")
        print("\033[1;31mThis is your new production list\033[0m".center(50,"-"))
        for i in product_list:       #打印新的产品清单
            print(count,i)
            count+=1
    elif select == 'm':
        modify_index = input("Please input index of the item which you want to modify:")    #输入要修改价格的产品序号
        modify_index = int(modify_index)
        length = product_list.index(product_list[-1])   #判断输入的修改价格产品序号是否再产品清单范围
        if 0 <= modify_index <= length:
            new_price = input("Please input the new price:")                    #输入新的价格
            product_list[modify_index][1]=new_price                                 #将新的价格修改至产品清单列表中
            with open("product_list","w") as f_modify:                          #想修改的产品清单列表写入文件中
                for i in product_list:
                    f_modify.writelines(i[0]+","+i[1]+"\n")
            print("\033[1;31mThis is your new production list\033[0m".center(50,"-"))
            for i in product_list:                                        #打印新的产品清
                print(count,i)
                count+=1
        else:
            print("Your select is invalid, Please try again!")      #如果输入的序号不在范围内，则报错重新来
    elif select == 'd':                                             #删除商品
        delete_index = input("Please input index of the item which you want to delete:")
        delete_index = int(delete_index)
        length = product_list.index(product_list[-1])               #判断输入的删除序号是否再产品清单范围
        if 0 <= delete_index <= length:
            product_list.pop(delete_index)                      #从产品清单中删除制定的产品
            with open("product_list","w") as f_del:
                for i in product_list:
                    f_del.writelines(i[0]+","+i[1]+"\n")           #将新的产品清单写入文件中
            print("\033[1;31mThis is your new production list\033[0m".center(50,"-"))
            for i in product_list:
                print(count,i)
                count+=1
        else:
            print("Your select is invalid, Please try again!")

    elif select == "q":
        print("You have been quit!")
        break
    else:
        print("invalid input,please input again!")













