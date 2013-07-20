from flask import Flask
from model import user
import config
from utility import guid

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Vela!'

@app.route('/user/register', methods=['POST'])
def user_register():
    if request.form['email'] and request.form['password']:
        exist_user = user.User({'email': request.form['email']})
        if exist_user.password:
            'ec' = 1062
            'em' = 'Email already exists'
        user_id = guid.new('user')
        user.User({'id': user_id})
        
    

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)