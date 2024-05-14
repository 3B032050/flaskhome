# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 15:04:03 2024

@author: user
"""

from flask import Flask, render_template ,request
from flask import redirect, url_for, session
from datetime import timedelta
import hashlib
import psycopg2
import dbconn

app = Flask(__name__, template_folder='templates',
            static_url_path='/static', static_folder='static')
app.secret_key = 'fd4723e200261a2271ea912571eaaald'
app.permanent_session_lifetime = timedelta(minutes=3)
name = ''

# DB Connection
def get_db_connection():
    conn = psycopg2.connect(
        host=dbconn.host,
        database=dbconn.database,
        user=dbconn.user,
        password=dbconn.password)
    return conn

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

'''@app.route('/user/<username>', methods=["GET"])
def user(username):
    message= request.args.get("message")
    return render_template('user.html', name=name)'''

@app.route('/user')
def user():
    if 'username' in session:
        username = session['username']
        return render_template('user.html', name=username)
    else:
        return redirect(url_for('signin'))

@app.route('/member/signin')
def signin():
    return render_template('member/signin.html')
'''@app.route('/member/login', methods=["POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        userpassword = request.form['userpassword']
        message = '登入成功!'
        return redirect(url_for('user', username=username, message=message))
    else:
        render_template("member/signin.html")'''
@app.route('/member/login', methods=["GET","POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        userpass = request.form['userpassword']
        md = hashlib.md5()
        md.update(userpass.encode('utf-8'))
        hashpass = md.hexdigest()
        conn = get_db_connection()
        cursor = conn.cursor()
        SQL = f"SELECT username, userpass FROM account WHERE username='{username}';"
        cursor.execute (SQL)
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        if not user:
            return redirect(url_for('signin'))

        if (username == user [0] and hashpass == user[1]):
            session.parmanent = True
            session['username'] = username
            return redirect(url_for('user'))
        else:
            return redirect(url_for('signin'))
    else:
        if 'username' in session:
            return redirect(url_for('user'))

        return render_template("member/signin.html")
'''@app.route('/member/login', methods=["GET","POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        userpass = request.form['userpassword']
        md = hashlib.md5()
        md.update(userpass.encode('utf-8'))
        hashpass = md.hexdigest()
        conn = get_db_connection()
        cursor = conn.cursor()
        SQL = f"SELECT username, userpass FROM account WHERE username='{username}';"
        cursor.execute(SQL)
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        if user and hashpass == user[1]:
            session.permanent = True
            session['username'] = username
            return redirect(url_for('user'))
        else:
            return render_template("member/signin.html")
    else:
        if 'username' in session:
            return redirect(url_for('user'))
        return render_template("member/signin.html")'''
'''@app.route('/user/<username>')
def user(username):
    global name
    name = username
    return render_template('user.html', name=username)'''

@app.route('/search', methods=['GET', 'POST'])
def search():
    '''global name
    username = name'''
    if 'username' in session:
        username = session['username']
    if request.method =='POST':
        keyword = request.values['keyword']
        if keyword == '紅燈':
            message = '紅燈停!'
        elif keyword == '黃燈':
            message = '加速通過馬路或停下等候綠燈!'
        elif keyword == '綠燈':
            message = '綠燈行!'
        else:
            message = '請重新輸入!'
        return render_template('user.html', name=username, message=message)
    else:
        message = '請使用HTTP POST傳送資料!'
        return render_template('result.html', message=message)

@app.route('/user/<name>/<surname>')
def user_surname(name,surname):
    return f'<h1>Hello, {name} {surname}!</h1>'

@app.route('/about')
def about():
    return '<h1>Hello</h1>'
if __name__ == '__main__':
    app.run()