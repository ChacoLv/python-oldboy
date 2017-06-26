# -*- coding:utf-8 -*-
# LC
'''
def search(*args):                              #查找Haproxy文件中的服务器
    list1 = []
    with open("haproxyfile","r") as f:
        flag = False
        for line in f:
            if line.strip() == "backend %s" % args:             #查找第一个以backend + 输入域名的起头的backend，将相关信息记录list中
                flag = True
                list1.append(line.strip())
                continue                                        #并继续循环，为了将backend下一行执行，即按着flag = True执行
            if line.strip().startswith("backend") or line.strip() == "":              #查到第二个backend这将flag置于Fasle,如果是空行，也将flag置于Fasle中，（防止文章末尾有多个空行）
                flag = False
            if flag:
                list1.append(line.strip())                  #将正确backend的后续信息继续记录至list中
        return list1


def delete(string):
    dict = eval(string)
    backend = dict["backend"]
    record = dict["record"]
    new_file_list = []
    if backend in domain_list():                        #判读要删除的域名是否在文件内
        with open("haproxyfile","r",encoding="utf-8") as f_read:
            for line in f_read:
                new_file_list.append(line)                          #读取文件的每行，将每行写入列表
                if line.strip() == "backend %s" %backend:           #如果有符合的backend，则将最近的写入列表弹出
                    new_file_list.pop()
                if line.strip() == "server %s weight %s maxconn %s" %(record["server"],record["weight"],record["maxconn"]):#如果有符合的server信息，则将最近的写入列表弹出
                    new_file_list.pop()
        with open("haproxyfile1", "a") as f_write:              #将删除后的写入文件中
            for line in new_file_list:
                f_write.write(line)
    else:
        print("The Domain not in this file!")

def add(string):                                    #增加ha文件配置服务器信息
    dict = eval(string)
    backend = dict["backend"]
    record = dict["record"]
    with open("haproxyfile","a") as f_write:
        f_write.write("backend %s\n"%backend)
        f_write.write("\t\tserver %s %s weight %s maxconn %s"%(record["server"][0],record["server"][1],
                                                            record["weight"],
                                                            record["maxconn"]))


def domain_list():                #将文件中所有的domain都摘出来
    backend_name = []
    with open("haproxyfile","r") as f_read:
        for line in f_read:
            if line.startswith("backend"):
                domain_name = line.split()[1]
                backend_name.append(domain_name)
    return backend_name

#域名信息查找
domain_search_name = input("Please input the domain your search:")
if domain_search_name in domain_list():
    domain_info = search(domain_search_name)
    print(domain_info)

#域名信息删除

string = "{'backend': 'www.yst.com.cn','record':{'server':'1.1.1.1','weight': 30,'maxconn': 2300}}"
delete(string)

#域名信息增加
string = "{'backend': 'www.yst.com.cn','record':{'server':'1.1.1.1','weight': 30,'maxconn': 2300}}"
add(string)

'''
#收集backend信息和对应server的信息
def backend_info():
    with open("haproxyfile","r") as f_read:
        backend_list = []
        dict_all = {}
        dict_ser = {}
        server_list = []
        for line in f_read:
            if line.strip().startswith("backend"):
                backend_name = line.split()[1]
                backend_list.append(backend_name)
                server_list = []
            if line.strip().startswith("server"):
                dict_ser['server'] = line.strip().split()[1]
                dict_ser['weight'] = line.strip().split()[3]
                dict_ser['maxconn'] = line.strip().split()[5]
                server_list.append(dict_ser)
                dict_all[backend_name] = server_list
    return backend_list,dict_all                #返回backend的所有域名信息和域名包含的服务器信息

