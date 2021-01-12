import connection
import purchaser_module

class Group:
    def __init__(self, user_name, group_name, item_name, max_price, category_id, end_time_day, end_time_time, id=-1):
        self.group_name = group_name
        self.item_name = item_name
        self.max_price = int(max_price)
        self.manager = user_name

        self.category_id = category_id
        self.end_date = end_time_day 
        self.end_time = end_time_time + ":00"
        if id != -1:
            self.id = id


def add(group):

    # query  = '''INSERT INTO groups(group_name, item_name, max_price, category_id, manager, end_date, end_time) 
    # VALUES('{}', '{}', {}, {}, '{}', '{}', '{}')'''.format(group.group_name, group.item_name, group.max_price,
    # group.category_id, group.manager, group.end_date, group.end_time)
    # connection.do_query_with_change(query)

    group_id = get_id_group(group)

    purch = purchaser_module.Purchaser(group.manager, group_id)
    if purchaser_module.add(purch):
        return True
    return False

def get_id_group(group):
    query = '''SELECT id FROM groups 
    WHERE group_name = '{}' and manager = '{}'  '''.format(group.group_name, group.manager)
    res = connection.do_query(query)
    if res:
        return res[0].get("id", 0)
    return None

group = Group("sari", "tables", "chair", 250, 1, '2021-12-02', '18:00')
print(add(group))
        
   