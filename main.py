from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
<<<<<<< HEAD
    return 'Hello guy. '
=======
    return 'Hello guy, This is an example of flask App that.'
>>>>>>> 540bf31131665393ade7cd21ddbf91837d414b33


