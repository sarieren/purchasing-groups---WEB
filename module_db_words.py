from config_db import *


def check_if_word_exists(id, word):
    try:
        with connection.cursor() as cursor:
            query = "SELECT * FROM db_word WHERE id=%s AND word=%s"
            val = (id, word)
            cursor.execute(query, val)
            result = cursor.fetchall()
            return result
    except:
        raise Exception("db_words Error")


def update_quantity(id, word, quantity=0):
    try:
        with connection.cursor() as cursor:
            query = "UPDATE db_word SET quantity=%s WHERE id=%s AND word=%s"
            val = (quantity, id, word)
            cursor.execute(query, val)
            connection.commit()
    except:
        raise Exception("db_words Error")


def insert_word(id, word):
    try:
        with connection.cursor() as cursor:
            query = "INSERT INTO db_word (id, word, quantity) VALUES (%s, %s, %s)"
            val = (id, word, '1')
            cursor.execute(query,val)
            connection.commit()
    except:
        raise Exception("db_words Error")

def get_words_sorted_descending_order(id):
    try:
        with connection.cursor() as cursor:
            query = "SELECT word FROM db_word WHERE id=%s ORDER BY quantity desc"
            val = (id)
            cursor.execute(query, val)
            result = cursor.fetchall()
            return result
    except:
        raise Exception("db_words Error")
    '''
        except Exception as e:
        return e
    '''


def word_update_or_insert(id, word):
    try:
        answer = check_if_word_exists(id, word)
        if answer != ():
            quantity = answer[0]["quantity"] + 1
            update_quantity(id, word, quantity)
        else:
            insert_word(id, word)
    except Exception as e:
        return e

