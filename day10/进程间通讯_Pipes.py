from multiprocessing import Process,Pipe
import os


#Pipe通过管道通信，数据传输，本质是通过socket进行数据交互

def f(conn):
    conn.send("hello world")
    print(conn.recv(),"My name is Mark")
    print(os.getppid(),os.getpid())
    conn.close()


if __name__ == "__main__":
    parent_conn,child_conn = Pipe()         #管道的两端可以通过socket进行数据交互
    print("---",os.getppid(),os.getpid())
    p = Process(target=f,args=(child_conn,))
    p.start()
    parent_conn.send("what is your name")
    print(parent_conn.recv())
    p.join()
