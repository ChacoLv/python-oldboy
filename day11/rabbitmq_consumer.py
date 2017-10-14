import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

channel = connection.channel()


channel.queue_declare('hello')

def callback(ch,method,properties,body):
    print("received body %s"%body)

channel.basic_consume(callback,                 #消费消息，这里表示如果有收到消息，则带哦用callback来处理收到的消息，则调用callback来打印收到的消息
                queue='hello',              #在那个队列中收取消息
                no_ack=True)


print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()