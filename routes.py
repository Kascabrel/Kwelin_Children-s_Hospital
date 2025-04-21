from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object('config.Config')


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/hello')
def hello():
    return 'Hello, World!'


@app.route('/about')
def goodbye():
    return 'Goodbye, World!'
