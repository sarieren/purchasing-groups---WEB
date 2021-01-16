from config_db import connection



def get_state(id):
    try:
        with connection.cursor() as cursor:
            query = "select _state from db_state where id = {}".format(id)
            cursor.execute(query)
            result = cursor.fetchall()
            if result:
                return result[0]["_state"]
            return None
    except:
        raise Exception("db_state error")


def insert_state(id, state):
    try:
        with connection.cursor() as cursor:
            query = "insert into db_state value('{}', '{}')".format(id, state)
            cursor.execute(query)
            connection.commit()
    except:
        raise Exception("db_state error")


def update_state(id, state):
    try:
        with connection.cursor() as cursor:
            query = "update db_state set _state = '{}' where id = {}".format(state, id)
            cursor.execute(query)
            connection.commit()
    except:
        raise Exception("db_state error")


def insert_or_update_state(id, state):
    try:
        check_have_state = get_state(id)
        if(check_have_state):
            update_state(id, state)
        else:
            insert_state(id, state)
    except Exception as e:
        return e
