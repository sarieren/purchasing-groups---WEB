from flask import Flask, render_template, request, redirect, url_for, make_response
from db.user_module import User

app = Flask(__name__, static_url_path='', static_folder='static',
template_folder= 'templates')


@app.route('/')
def root():
    return app.send_static_file('login.html')

@app.route('/submit_login', methods = ['POST'])
def authenticate():
    is_logged_in = request.cookies.get('logged_in')
    data = request.form
    user_name = data['user_name']
    password = data['password']   
    is_authorized = True #model.authenticate(user_name, password)
    if is_authorized:
        resp = make_response(app.send_static_file('index.html'))
        resp.set_cookie('logged_in', 'True')
        resp.set_cookie('username', user_name)
        return resp
    else:
        return redirect(url_for('root'))

# @app_route('/register', methods = ['POST'])
# def register_new_purchaser():
#     pass

app.run(port=3000, debug = 1)