import db.connection as connection


class Forums:
    def __init__(self, group_id, user_name, message_, end_date = "", end_time = ""):
        self.group_id = group_id
        self.user_name = user_name
        self.message_ = message_
        self.count_like = 0

        if end_date:
            self.end_date = end_date
            self.end_time = end_time
        




def sign_up(user):

    query = '''INSERT INTO forums 
    VALUES('{}', '{}', '{}')'''.format(user.user_name, user.user_mail, user.user_password)
    connection.do_query_with_change(query)