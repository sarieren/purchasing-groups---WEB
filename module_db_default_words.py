from config_db import connection


def get_number_of_words():
    try:
        with connection.cursor() as cursor:
            query_count = "SELECT COUNT(word) FROM db_defult_words;"
            cursor.execute(query_count)
            count = cursor.fetchall()
            return count
    except:
        raise Exception("DBError -  db default words")


def find_words_unused(num):
    try:
        num=min(num,get_number_of_words())
        with connection.cursor() as cursor:
            query_count = "SELECT COUNT(word) FROM db_defult_words where in_use=0;"
            cursor.execute(query_count)
            count = cursor.fetchall()
            if(count[0]["COUNT(word)"]<num):
                restart_table()
            query = "SELECT * FROM db_defult_words where in_use=0 limit " +str(num)+";"
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
                result = cursor.fetchall()
    except:
        raise Exception("DBError -  db default words")


def restart_table():
    try:
        with connection.cursor() as cursor:
            query = "UPDATE db_defult_words set in_use = 0;"
            cursor.execute(query)
            result = cursor.fetchall()
    except:
        raise Exception("DBError -  db default words")


def test():
    if connection.open:
        print("the connection is opened")
    with connection.cursor() as cursor:
        query = "SELECT * FROM db_defult_words"
        cursor.execute(query)
        result = cursor.fetchall()
        print(result)
        print(find_words_unused(5))
        query = "SELECT * FROM db_defult_words"
        cursor.execute(query)
        result = cursor.fetchall()
        print("main")
        print(result)


