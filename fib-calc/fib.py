import pika
import os, sys
from time import sleep
import daemon

# fpid = os.fork()
# if fpid != 0:
#     sys.exit(0)

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
    print ("Fib Result: %s" % response)
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     body=str(response))
    print("Sent Reponse")

connected = False
while not connected:
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters('messagequeue'))
        connected = True
    except:
        print("Could not connect to queue: messagequeue")
        sleep(5)
channel = connection.channel()
channel.queue_declare(queue='rpc_queue')

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='rpc_queue', auto_ack=True, on_message_callback=on_request)

print(" [x] Awaiting RPC requests")
channel.start_consuming()
