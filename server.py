from flask import Flask, render_template, request, redirect, url_for, make_response, Response
from db.user_module import User
import db.user_module as user_module
import db.category_module as category_module
import db.group_module as group_module
import db.purchaser_module as purchaser_module
import json

app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')


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
        # pop error message
        return app.send_static_file('login.html')


@app.route('/submit_new_group', methods=['POST'])  # have to change route to "groups"
def submit_new_group():
    user_name = request.cookies.get('username')
    data = request.form
    print(user_name)
    group_name = data['group_name']
    item_name = data['item_name']
    max_price = data['max_price']
    category = data['category']
    end_time_day = data['end_time_day']
    end_time_time = data['end_time_time']
    group_description = data['group_description']
    category_id = category_module.get_id_from_name(category)
    group = group_module.Group(user_name, group_name, item_name, max_price, category_id, end_time_day, end_time_time, group_description)
    is_added = group_module.add(group)

    if not is_added:
        return {}, 500
    return group.__dict__, 201  # app.send_static_file("index.html")


@app.route('/new_group', methods=['GET'])
def get_add_new_group():
    is_logged_in = request.cookies.get('logged_in')
    if is_logged_in == "True":
        categories = category_module.get_list_all_categories()
        return render_template("add_group.html", categories=categories)
    else:
        return redirect(url_for('login'))


@app.route("/groups")
def get_all_gruops():
    return Response(json.dumps([G.__dict__ for G in group_module.get_all_groups()]), 200)


@app.route("/categories")
def get_all_categories():
    return Response(json.dumps(category_module.get_all_categories()), 200)


@app.route("/groups/<user_name>")
def get_groups_for_user(user_name):
    return Response(json.dumps([G.__dict__ for G in group_module.get_all_groups_of_user_name(user_name)  ]), 200)


@app.route("/groups_by_category/<category_name>")
def get_group_by_category(category_name):
    return Response(json.dumps([G.__dict__ for G in group_module.get_all_groups_by_categoty_name(category_name)  ]), 200)


@app.route("/users")
def get_all_users():
    return Response(json.dumps([U.__dict__ for U in user_module.get_all_users()  ]), 200)


@app.route("/users/<user>")
def get_user_details(user):
    return Response(json.dumps(user_module.get_user_by_name(user).__dict__), 200)

    
@app.route("/categories", methods=["POST"])
def add_category():
    #add(category object) in category_module
    pass
@app.route("/purchasers", methods=["POST"])
def add_purchaser_to_group():
    #add(purchaser) in purchaser module
    pass


# #OPTIONAL
# @app.route("/imgs/users/<user>")
# def get_user_profile(user):
#     pass

# @app.route("/imgs/groups/<group_id>")
# def get_groups_product_imgs(group_id):
#     pass

# @app.route("/forums/groups/<group_id>")
# def get_forum_msgs_for_group(group_id):
#     pass




#imgs of products , forum, emails


app.run(port=3000, debug=1)
