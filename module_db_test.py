from config_db import *
from module_db_words import *
from module_db_default_words import *


def insert_words_test(id, list_words):
    index = 0
    try:
        for word in list_words:
            with connection.cursor() as cursor:
                query = "INSERT INTO db_test (id, word, _index) VALUES (%s, %s, %s)"
                val = (id, word, index)
                cursor.execute(query, val)
                connection.commit()
                index+=1
    except:
        raise Exception("db_test Error")

def get_words_from_test(id):
    try:
        with connection.cursor() as cursor:
            query = "SELECT word FROM db_test WHERE id=%s ORDER BY _index"
            val = (id)
            cursor.execute(query, val)
            result = cursor.fetchall()
            return result
    except:
        raise Exception("db_test Error")

def delete_words_from_test(id):
    try:
        with connection.cursor() as cursor:
            query = "DELETE FROM db_test WHERE id=%s"
            val = (id)
            cursor.execute(query, val)
            connection.commit()
    except:
        raise Exception("db_test Error")


def find_words_for_test(id, amout_of_words_translate):
    try:
        new_word_list = []
        list_words = get_words_sorted_descending_order(id)
        for word in list_words:
            new_word_list.append(word["word"])

        if len(new_word_list) < amout_of_words_translate:
            left_to_add = amout_of_words_translate - len(new_word_list)
            left_to_add_list = find_words_unused(left_to_add)
            left_to_add_list = [word["word"] for word in left_to_add_list]
            new_word_list = new_word_list + left_to_add_list

        elif len(new_word_list) > amout_of_words_translate:
            new_word_list = new_word_list[:amout_of_words_translate]
        return new_word_list
    except Exception as e:
        return e



#Insert_words_test(1, ["why", "how","chair", "table"])
# Insert_words_test(2, ["a", "b","c", "d"])

# print(get_words_from_test(2))
# delete_words_from_test(2)

# print(find_words_for_test(33, 6))