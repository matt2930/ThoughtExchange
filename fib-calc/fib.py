import pika
import os, sys
from time import sleep

fpid = os.fork()
if fpid != 0:
    sys.exit(0)

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='rpc_queue')

def fib(n):
    a = 0
    b = 1
    c = None
    for i in range(1,n):
        c = a + b
        a = b
        b = c
    return c


def on_request(ch, method, props, body):
    n = int(body)
    print(" [.] fib(%s)" % n)
    response = fib(n)
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                        props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='rpc_queue',on_message_callback=on_request)

print(" [x] Awaiting RPC requests")
channel.start_consuming()
