import db.connection as connection
import db.purchaser_module as purchaser_module


class Group:
    def __init__(self, user_name, group_name, item_name, max_price, category_id, end_time_day, end_time_time, description, id=-1):
        self.group_name = group_name
        self.item_name = item_name
        self.max_price = int(max_price)
        self.manager = user_name

        self.category_id = category_id
        self.end_date = end_time_day 
        self.end_time = end_time_time + ":00"
        self.description = description
        if id != -1:
            self.id = id


def add(group_):
    query = '''INSERT INTO `groups`(group_name, item_name, max_price, category_id, manager, end_date, end_time) 
    VALUES('{}', '{}', {}, {}, '{}', '{}', '{}', '{}')'''.format(group_.group_name, group_.item_name, group_.max_price,
                                                           group_.category_id, group_.manager, group_.end_date, group_.end_time,
                                                           group_.description)
    connection.do_query_with_change(query)

    group_id = get_id_group(group_)

    purch = purchaser_module.Purchaser(group_.manager, group_id)
    if purchaser_module.add(purch):
        return True
    return False


def get_id_group(group_):
    query = '''SELECT id FROM `groups`
    WHERE group_name = '{}' and manager = '{}'  '''.format(group_.group_name, group_.manager)
    res = connection.do_query(query)
    if res:
        return res[0].get("id", 0)
    return None
