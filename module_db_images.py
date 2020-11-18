from config_db import connection


def get_word_image():
    try:
        with connection.cursor() as cursor:
            query = "SELECT word from db_image where _index = {};".format(0)
            cursor.execute(query)
            result = cursor.fetchall()
            if result == ():
                restart_index_col()
            query = "SELECT word FROM db_image where _index = {};".format(0)
            cursor.execute(query)
            result = cursor.fetchall()[0]["word"]
            update_in_use(result)
            return result

    except:
        raise Exception("db_image error")

def update_in_use(result):
    try:
        with connection.cursor() as cursor:
            query = "UPDATE db_image set _index = {} where word = %s;".format(1)
            val = (result)
            cursor.execute(query, val)
            connection.commit()
    except:
        raise Exception("DBError -  db image")


def restart_index_col():
    try:
        with connection.cursor() as cursor:
            query = "UPDATE db_image set _index = 0;"
            cursor.execute(query)
            connection.commit()
    except:
        raise Exception("DBError - db image")

