from flask import Flask, render_template, request, redirect
import pika

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        return redirect('/fib')

@app.route('/fib')
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

    channel.basic_publish(routing_key='rpc_queue', body=str(num))

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
