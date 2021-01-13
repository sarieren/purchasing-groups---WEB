# import pymysql
# from db.my_config import DB_HOST, DB_USER, DB_PASSWORD

import mysql.connector
from mysql.connector import errorcode


# Obtain connection string information from the portal
config = {

    'host': "groupbuy1234.mysql.database.azure.com",
    'user': 'groupbuyuser@groupbuy1234',
    'password': 'GroupBuy1234',
    'database': 'group_buy'
}

# Construct connection string
try:
    connection = mysql.connector.connect(**config)
    print("Connection established")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with the user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)


def do_query_with_change(query_str):
    connection = mysql.connector.connect(**config)

    with connection.cursor() as cursor:
        cursor.execute(query_str)
        connection.commit()

    connection.close()
    return True


def do_query(query_str):
    connection = mysql.connector.connect(**config)

    with connection.cursor() as cursor:
        cursor.execute(query_str)
        result = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        rows = [dict(zip(columns, row)) for row in result]

    connection.close()
    return rows


# print(do_query("select * from groups"))