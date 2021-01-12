from flask import Flask, render_template, request, redirect, url_for, make_response, flash
from db.user_module import User
import db.user_module as user_module

app = Flask(__name__, static_url_path='', static_folder='static',
template_folder= 'templates')


@app.route('/')
def root():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return app.send_static_file('login.html')

@app.route('/submit_login', methods = ['GET'])
def authenticate_url():
    is_logged_in = request.cookies.get('logged_in')
    if is_logged_in == 'True':
        return app.send_static_file('index.html')
    else:
        return redirect(url_for('login'))


@app.route('/submit_login', methods = ['POST'])
def authenticate():
    is_logged_in = request.cookies.get('logged_in')
    data = request.form
    user_name = data['user_name']
    password = data['password']   
    is_authorized = user_module.authenticate(user_name, password)
    if is_authorized:
        resp = make_response(app.send_static_file('index.html'))
        resp.set_cookie('logged_in', 'True')
        resp.set_cookie('username', user_name)
        return resp
    else:
        return redirect(url_for('root'))

@app.route('/register', methods = ['POST'])
def register_new_purchaser():
    data = request.form
    user_name = data['user_name']
    password = data['password']
    email = data['email']
    new_purchaser = User(user_name, email, password)
    registeration_status = user_module.sign_up(new_purchaser)
    if registeration_status:
        resp = make_response(app.send_static_file('index.html'))
        resp.set_cookie('logged_in', 'True')
        resp.set_cookie('username', user_name)
        return resp
    else:
        #pop error message 
        return app.send_static_file('login.html')




app.run(port=3000, debug = 1)