import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="englishbot",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)
