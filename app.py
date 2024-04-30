# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 15:04:03 2024

@author: user
"""

from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return '<h1>Hello Flask</h1>'

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/user/<name>/<surname>')
def user_surname(name,surname):
    return f'<h1>Hello, {name} {surname}!</h1>'

@app.route('/about')
def about():
    return '<h1>Hello</h1>'
if __name__ == '__main__':
    app.run()