import pymysql
from my_config import DB_HOST, DB_USER, DB_PASSWORD

connection = pymysql.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    db="group_buy",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)


def do_query_with_change(query_str):
    with connection.cursor() as cursor:
        cursor.execute(query_str)
        connection.commit()
        return True


def do_query(query_str):
    with connection.cursor() as cursor:
        cursor.execute(query_str)
        result = cursor.fetchall()
        return result