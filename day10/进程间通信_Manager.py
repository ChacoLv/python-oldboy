from multiprocessing import Process,Manager
import os

def f(dict,lis):
    dict[1] = 1
    dict[2] = 2
    dict[os.getppid()] = os.getppid()
    dict[os.getpid()] = os.getpid()
    lis[2] = lis[2] + 1



if __name__ == "__main__":
    with Manager() as manager:
        d = manager.dict()              #通过manager方法，生成一个字典，字典可以在多进程之间共享数据，并修改
        l = manager.list(range(5))      #通过manager方法，生产一个列表，列表可以在多进程之间进行数据共享
        print("----",l)
        p_list = []


        for i in range(5):
            p = Process(target=f,args=(d,l))
            p.start()
            p_list.append(p)

        for res in p_list:
            res.join()

        print(d)
        print(l)

