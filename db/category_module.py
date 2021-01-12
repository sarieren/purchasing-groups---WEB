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


print(get_list_all_categories())