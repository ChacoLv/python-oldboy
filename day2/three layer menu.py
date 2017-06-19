# -*- coding:utf-8 -*-
# LC
data = {
    "浙江省":{
        "杭州市":{
            "西湖区":["西湖","黄龙"],
            "余杭区":["西溪银泰","闲湖"],
            "滨江区":["星光大道","垃圾街"]
        },
        "温州市":{
            "瓯海区":["温州大学","茶山"],
            "苍南":["金乡","灵溪"]
        },
        "台州":{
            "路桥":["海鲜","喷雾器"],
            "温岭":["高山","绿叶"]
        }
    },
    "广东省":{
        "广州市"
    }
}

exit_flag = True

while exit_flag:
    for i in data:
        print(i)
    choice = input("请选择1>>>:")                  #选择省
    if choice in data:
        while exit_flag:
            for j in data[choice]:
                print(j)
            choice2 = input("请选择2,返回上一层请按b,退出请按q>>>:")         #选择市
            if choice2 in data[choice]:
                while exit_flag:
                    for k in data[choice][choice2]:
                        print(k)
                    choice3 = input("请选择3,返回上一层请按b,退出请按q>>>:")     #选择区
                    if  choice3 in data[choice][choice2]:
                        for l in data[choice][choice2][choice3]:
                            print(l)
                        choice4 = input("最后一层,返回上一层请按b,退出请按q>>>:")
                        if choice4 == "b":
                            break
                        elif choice4 == "q":
                            exit_flag = False
                    elif choice3 == "b":            #如果选择返回，则中断此次循环
                        break
                    elif choice3 == "q":            #如果选择退出，则将循环值改为False，所有循环结束，退出
                        exit_flag = False
                    else:
                        print("选择有误，重新输入！")
                        continue
            elif choice2 == "b":
                break
            elif choice2 == "q":
                exit_flag = False
            else:
                print("选择有误，重新输入！")
                continue









