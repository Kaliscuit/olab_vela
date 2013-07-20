from flask import Flask
import config
from utility import guid 

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello Vela!'
    

@app.route('/new_id'):
def new_id():
    id = guid.new('user')
    return id


if __name__ == '__main__':
    app.run()
