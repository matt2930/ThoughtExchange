from flask import Flask, render_template, request, redirect
import pika

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
        return render_template('index.html')


@app.route('/fib', methods=['POST'])
def index2():
    num = request.form['number']
    connected = False
    while not connected:
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters('messagequeue'))
            connected = True
        except:
            print("Could not connect")
    channel = connection.channel()
    channel.queue_declare(queue='rpc_queue')
    result = channel.queue_declare(queue='response')
    callback_queue = result.method.queue
    channel.basic_publish(exchange='', 
                          routing_key='rpc_queue',
                          properties=pika.BasicProperties(
                            reply_to = callback_queue
                            ), 
                          body=str(num))
    connection.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
