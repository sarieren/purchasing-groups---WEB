from config_db import connection


def get_number_of_words():
    try:
        with connection.cursor() as cursor:
            query_count = "SELECT COUNT(word) as count FROM db_defult_words;"
            cursor.execute(query_count)
            count = cursor.fetchall()
            return count[0]["count"]
    except:
        raise Exception("DBError -  db default words")


def find_words_unused(num):
    try:
        number_of_words = get_number_of_words()
        num = min(num, number_of_words)
        with connection.cursor() as cursor:
            query_count = "SELECT COUNT(word) as count FROM db_defult_words where in_use=0;"
            cursor.execute(query_count)
            count = cursor.fetchall()
            if(count[0]["count"] < num):
                restart_table()
            query = "SELECT word FROM db_defult_words where in_use = 0 limit " + str(num) + ";"
            cursor.execute(query)
            result = cursor.fetchall()
            update_in_use(result)
            return result
    except Exception as e:
        return e


def update_in_use(words):
    try:
        c='"'
        with connection.cursor() as cursor:
            for word in words:
                query = "UPDATE db_defult_words set in_use = 1 where word = "+c+ word["word"] +c+";"
                cursor.execute(query)
                connection.commit()
    except:
        raise Exception("DBError -  db default words")


def restart_table():
    try:
        with connection.cursor() as cursor:
            query = "UPDATE db_defult_words set in_use = 0;"
            cursor.execute(query)
            connection.commit()
    except:
        raise Exception("DBError -  db default words")
