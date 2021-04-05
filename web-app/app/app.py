from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/fib', methods=['POST'])
def index2():
    num = request.form['number']
    return '<h1>Test %s </h1>' % num

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
