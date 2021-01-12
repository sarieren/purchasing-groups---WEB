import connection as connection


class Purchaser:
    def __init__(self, user_name, group_id):
        self.user_name = user_name
        self.group_id = group_id
        

def add(purchaser):
    if not exist(purchaser):
        query = '''INSERT INTO purchaser
        VALUES('{}', {})'''.format(purchaser.user_name, purchaser.group_id)
        connection.do_query_with_change(query)
        return True
    else:
        return False


def exist(purchaser):
    query = '''SELECT count(*) FROM purchaser 
    WHERE user_name = '{}' and group_id = {} '''.format(purchaser.user_name, purchaser.group_id)
    res = connection.do_query(query)
    if res[0].get('count(*)') > 0:
        return True
    return False


def get_id_group_by_name(name):

    query = '''SELECT group_id FROM purchaser
    where user_name = '{}' '''.format(name)
    res = connection.do_query(query)

    groups = []
    for purchase in res:
        groups.append(purchase.get("group_id", 0))
    return groups

