import threading
import time



event = threading.Event()

def lighter():
    counter = 0
    event.set()     #事件set表示绿灯
    while True:
        counter += 1
        if counter <= 10: #表示绿灯时间为10秒，
            print("\033[42;1m lighter is green， car go...\033[0m,count is %s" %counter)
        elif counter > 10 and counter <= 15:
            print("\033[41;1m lighter is red, car stop...\033[0m,count is %s"%counter)
            event.clear()   #事件clear表示将绿灯设置为红灯,红灯执行5秒
        else:
            event.set()     #红灯完成后，即将红灯设置为绿灯，并清空计数器
            counter = 0
        time.sleep(1)

def car(car_name):
    while True:
        if event.is_set():
            print("lighter is green, %s can go"%car_name)
            time.sleep(1)
        else:
            print("lighter is red ,%s can not go ,stop"%car_name)
            event.wait()        #监控事件，如果event未被set，则wait，如果set后，则进入set状态，即绿灯
            print("ligher changed green，%s go ........")

light_hz = threading.Thread(target=lighter,)
light_hz.start()

car_lc = threading.Thread(target=car,args=("Cheng Lv's Golf Volkswagen",))
car_lc.start()


