from flask import Flask,rendor_template

app = Flask(__name__)
@app.route('/')
def index():
    return rendor_template('index.html')
@app.route('/hello')
def hello():
    return '<h1>Hello Flask</h1>'
@app.route('/user/<name>')
def user(name):
    return rendor_template('index.html',name=name)
@app.route('/user/<name>/<surname>')
def surname(name,surname):
    return f'<h1>Hello,{name}{surname}!</h1>'
if __name__ == '__main__':
    app.run()