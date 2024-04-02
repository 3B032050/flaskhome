from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Hello world</h1>'
@app.route('/hello')
def hello():
    return '<h1>Hello Flask</h1>'
@app.route('/user/<name>')
def user(name):
    return f'<h1>Hello,{name}!</h1>'
@app.route('/user/<name>/<surname>')
def surname(name,surname):
    return f'<h1>Hello,{name}{surname}!</h1>'
if __name__ == '__main__':
    app.run()