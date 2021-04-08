from flask import Flask, render_template, request, redirect

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
    # connection = pika.BlockingConnection(pika.ConnectionParameters('message-queue'))
    # channel = connection.channel
    return '<h1>Test %s </h1>' % num

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
