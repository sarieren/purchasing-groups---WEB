
import db.connection 



class User:
    def __init__(self, name, mail, password):
        self.user_name = name
        self.user_password = password
        self.user_mail = mail


def sign_up(user):

    if not exist(user):
        query  = '''INSERT INTO user 
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


def sign_in(user):
    query = '''SELECT count(*) FROM user 
    WHERE user_name = '{}' and user_mail = '{}' and user_password = '{}'  '''.format(user.user_name, user.user_mail, user.user_password)
    res = connection.do_query(query)
    if res[0].get('count(*)') > 0:
        return True
    return False

def get_user_by_name(name):
    query = '''SELECT * FROM user 
    WHERE user_name = '{}' '''.format(name)
    res = connection.do_query(query)
    if res:
        user = User(res[0].get("user_name", " "), res[0].get("user_mail", " "), res[0].get("user_password", " "))
        return user
    return None

