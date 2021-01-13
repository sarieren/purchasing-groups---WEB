import db.connection as connection


class Category:

    def __init__(self, category_name, category_id = -1):
        self.name = category_name
        if category_id != -1:
            self.id = category_id


def get_list_all_categories():
    
    query = '''SELECT * FROM category '''
    res = connection.do_query(query)

    categories = []
    for category in res:
        categories.append(category.get("name", ""))
    return categories


def get_id_from_name(name):

    query = '''SELECT id FROM category where name = '{}' '''.format(name)
    res = connection.do_query(query)

    if res:
        return res[0].get("id", 0)
    return None


def get_name_from_id(id_):

    query = '''SELECT name FROM category where id = {} '''.format(id_)
    res = connection.do_query(query)

    if res:
        return res[0].get("name", 0)
    return None

def add(category):
    if not exist(category):
        query = '''INSERT INTO category(name) 
        VALUES('{}')'''.format(category.name)
        connection.do_query_with_change(query)
        return True
    else:
        return False


def exist(category):
    query = '''SELECT count(*) FROM category 
    WHERE name = '{}' '''.format(category.name)
    res = connection.do_query(query)
    if res[0].get('count(*)') > 0:
        return True
    return False



def get_all_categories():
    # categories = []

    query = '''SELECT * FROM category'''
    res = connection.do_query(query)
    # for category in res:
    #     categories.append(get_group(group))

    return res

