from flask import Flask, render_template, request, redirect, url_for, make_response
from db.user_module import User
from db.category_module import get_list_all_categories

app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')


@app.route('/')
def root():
    return app.send_static_file('login.html')


@app.route('/submit_login', methods = ['POST'])
def authenticate():
    is_logged_in = request.cookies.get('logged_in')
    print(is_logged_in)
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


@app.route('/submit_new_group', methods=['POST'])
def submit_new_group():
    user_name = request.cookies.get('username')
    # print(user_name)
    data = request.form

    group_name = data['group_name']
    item_name = data['item_name']
    max_price = data['max_price']
    category = data['category']
    end_time_day = data['end_time_day']
    end_time_time = data['end_time_time']
    print("j")
    print(group_name, " ", type(group_name))
    print(item_name, " ", type(item_name))
    print(max_price, " ", type(max_price))
    print(category, " ", type(category))
    print(end_time_day, " ", type(end_time_day))
    print(end_time_time, " ", type(end_time_time))

    # group = Group(user_name, group_name, item_name, max_price, category_id, end_time_day, end_time_time)
    # is_added = db.group.add(group)


@app.route('/new_group', methods=['GET'])
def get_add_new_group():
    categories = get_list_all_categories()
    return render_template("add_group.html", categories=categories)


app.run(port=3000, debug=1)
