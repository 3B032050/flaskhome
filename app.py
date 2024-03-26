from flask import Flask

app = Flask(_name_)
@app.route('/')
def index():
    return '<h1>Hello world</h1>'