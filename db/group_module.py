import db.connection as connection
import db.purchaser_module as purchaser_module
import db.category_module as category_module


class Group:
    def __init__(self, user_name, group_name, item_name, max_price, category_id, end_time_day, end_time_time, description, id_=-1):
        self.group_name = group_name
        self.item_name = item_name
        self.max_price = int(max_price)
        self.manager = user_name

        self.category_id = category_id
        self.end_date = end_time_day
        self.end_time = end_time_time + ":00"
        self.description_group = description
        if id != -1:
            self.id_ = id_


def add(group_):
    print("group_ = \n", group_.group_name, group_.item_name, group_.max_price,
                                                                 group_.category_id, group_.manager, group_.end_date, group_.end_time,
                                                                 group_.description_group)
    query = '''INSERT INTO `groups`(group_name, item_name, max_price, category_id, manager, end_date, end_time, description_group) 
    VALUES('{}', '{}', {}, {}, '{}', '{}', '{}', '{}')'''.format(group_.group_name, group_.item_name, group_.max_price,
                                                                 group_.category_id, group_.manager, group_.end_date, group_.end_time,
                                                                 group_.description_group)
    print("********************", group_)
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


def get_all_groups():
    groups = []

    query = '''SELECT * FROM `groups`  NATURAL JOIN count_members_group WHERE groups.id = count_members_group.group_id'''
    res = connection.do_query(query)
    for group in res:
        count = group.get("count")
        del group["count"]
        groups.append((get_group(group), count))

    return groups


def get_all_groups_of_user_name(name):

    groups = []
    all_id_groups = purchaser_module.get_id_group_by_name(name)

    for id_ in all_id_groups:
        query = '''SELECT * FROM `groups`
        WHERE id = {} '''.format(id_)
        res = connection.do_query(query)
        if res:
            groups.append(get_group(res[0]))

    return groups


def get_group(dict_group):
    id_ = dict_group.get("id")
    group_name = dict_group.get("group_name")
    item_name = dict_group.get("item_name")
    max_price = dict_group.get("max_price")
    category_id = dict_group.get("category_id")
    manager = dict_group.get("manager")

    end_date = str(dict_group.get("end_date"))
    # [:len(dict_group.get("end_time"))-3]
    end_time = str(dict_group.get("end_time"))
    end_time = end_time[:len(end_time) - 3]
    description_group = dict_group.get("description_group")

    g = Group(manager, group_name, item_name, max_price, category_id,
              end_date, end_time, description_group, id_)
    return g


def get_all_groups_by_categoty_name(name):

    groups = []
    id_category = category_module.get_id_from_name(name)

    query = '''SELECT * FROM `groups`
    WHERE category_id = {} '''.format(id_category)
    res = connection.do_query(query)
    for group in res:
        groups.append(get_group(group))

    return groups


def get_count_member_by_group_id(id_):

    query = '''SELECT count(*) FROM purchaser 
    WHERE group_id = {}'''.format(id_)
    res = connection.do_query(query)

    return res[0].get('count(*)')


def get_id_groups():
    id_list = []
    query = '''SELECT id FROM `groups`'''
    res = connection.do_query(query)
    for id_ in res:
        id_list.append(id_.get("id"))
    return id_list


def get_all_gruops_without_preproccess():
    query = '''SELECT * FROM `groups`  NATURAL JOIN count_members_group WHERE groups.id = count_members_group.group_id'''
    res = connection.do_query(query)
    return list(res)





def get_all_user_name_by_group_id(group_id):

    query = '''select user_name, user_mail
    from (select id, manager from groups) as g
    natural join (select user_name, user_mail from user) as u
    where g.id = {} and u.user_name = g.manager'''.format(group_id)
    res = connection.do_query(query)

    return list(res)