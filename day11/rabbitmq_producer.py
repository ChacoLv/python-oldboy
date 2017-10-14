import pika         #pika是python用于调用rabbitmq的第三方函数
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')          #建立一个socket，即与rabbitmq的socket
)

channel = connection.channel()          #声明一个管道

channel.queue_declare(queue="hello")        #在频道中声明一个队列，用于消息传输

while True:
    channel.basic_publish(exchange='',routing_key='hello',body='I love python')         #需要通过队列"hello"来传输的body的内容
    print("发送消息")
    time.sleep(1)


connection.close()