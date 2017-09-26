from urllib.request import urlopen
import gevent,time
from gevent import monkey
import ssl

context = ssl._create_unverified_context()      #打开https的时候，传入ssl验证的上下文参数，以便能够正常urlopen

monkey.patch_all()              #表示将当前所有IO操作单独做上标记，通过gevent切换进程


def func(url):
    print("Get:%s"%url)
    resp = urlopen(url,context=context)
    data = resp.read()
    print("Have get %s size"%len(data))

urls = [
    "https://www.python.org/",
    "https://www.yahoo.com/",
    "https://www.github.com/"
]


syc_time = time.time()

for url in urls:
    func(url)               #串行执行任务，即通过串行的进行对url打开

print("sync total cost time:%s"%(time.time()-syc_time))


ansync_time = time.time()

gevent.joinall([                            #通过gevent结合monkey进行切换，以便实现任务之间切换
    gevent.spawn(func,"https://www.python.org/"),
    gevent.spawn(func,"https://www.yahoo.com/"),
    gevent.spawn(func,"https://www.github.com/")
])

print("ansync total cost time :%s"%(time.time()-ansync_time))