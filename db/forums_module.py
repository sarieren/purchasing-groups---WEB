import db.connection as connection
from datetime import datetime


class Forums:
    def __init__(self, group_id, user_name, message_, count_like = 0, end_date = "", end_time = ""):
        self.group_id = int(group_id)
        self.user_name = user_name
        self.message_ = message_
        self.count_like = count_like

        if end_date:
            self.end_date = end_date
            self.end_time = end_time
        




def add(forums):

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
 
    n = now.split(" ")

    query = '''INSERT INTO forums 
    VALUES({}, '{}', '{}', {}, '{}', '{}')'''.format(forums.group_id, forums.user_name, forums.message_, forums.count_like , n[0], n[1])
    connection.do_query_with_change(query)
    return True



def get_all_message_by_group_id_order(group_id):
    
    forums = []

    query = '''SELECT * FROM forums
    WHERE group_id = {} 
    ORDER BY end_date, end_time DESC'''.format(group_id)
    res = connection.do_query(query)
    for forum in res:
        forums.append(get_forum(forum))

    return forums


def get_forum(dict_forum):
    group_id = dict_forum.get("group_id")
    user_name = dict_forum.get("user_name")
    message_ = dict_forum.get("message_")
    count_like = dict_forum.get("count_like")
    end_date = dict_forum.get("end_date")
    end_time = dict_forum.get("end_time")

    f = Forums(group_id, user_name, message_, count_like, end_date, end_time)
    return f




