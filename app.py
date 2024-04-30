
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 15:04:03 2024

@author: user
"""

from flask import Flask, render_template ,request

app = Flask(__name__, template_folder='templates',
            static_url_path='/static', static_folder='static')

@app.route('/')
@app.route('/index',methods=['GET'])
def index():
    name = request.args.get('name')
    return render_template('index.html', **locals())

@app.route('/shopping')
def shopping():
    return render_template('shopping.html')

@app.route('/ticket')
def ticket():
    return render_template('ticket.html')

@app.route('/welfare')
def welfare():
    return render_template('welfare.html')

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
