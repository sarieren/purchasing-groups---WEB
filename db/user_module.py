import db.connection as connection


class User:
    def __init__(self, name, mail, password):
        self.user_name = name
        self.user_password = password
        self.user_mail = mail


def sign_up(user):

    if not exist(user):
        query = '''INSERT INTO user 
        VALUES('{}', '{}', '{}')'''.format(user.user_name, user.user_mail, user.user_password)
        connection.do_query_with_change(query)
        return True
    else:
        return False


def exist(user):
    query = '''SELECT count(*) FROM user 
    WHERE user_name = '{}' or user_mail = '{}'  '''.format(user.user_name, user.user_mail)
    res = connection.do_query(query)
    if res[0].get('count(*)') > 0:
        return True
    return False


def authenticate(user_name, password):
    query = '''SELECT count(*) FROM user 
    WHERE user_name = '{}' and user_password = '{}'  '''.format(user_name, password)
    res = connection.do_query(query)
    if res[0].get('count(*)') > 0:
        return True
    return False


def get_user_by_name(name):
    query = '''SELECT * FROM user 
    WHERE user_name = '{}' '''.format(name)
    res = connection.do_query(query)
    if res:
            return get_user(res[0])
    return None

def get_user(dict_user):
    
    user_name = dict_user.get("user_name")
    user_mail = dict_user.get("user_mail")
    user_password = dict_user.get("user_password")
    
    
    u = User(user_name, user_mail, user_password)
    return u


def get_all_users():
    users = []

    query = '''SELECT * FROM user'''
    res = connection.do_query(query)
    for user in res:
        users.append(get_user(user))

    return users



