from module_db_test import *
from translate_word import get_translate_word


def test_word(id, num=5):
    ls_of_test_word = find_words_for_test(id, num)
    insert_words_test(id, ls_of_test_word)
    string_to_return = ""
    for word in ls_of_test_word:
        string_to_return += word
        string_to_return += '\n'
    string_to_return += "answer by order with space between words"
    return string_to_return


def menu_test_word(id, input):
    try:
        if input == "/test":
            return test_word(id)
        else:
            return check_results(id, input)
    except Exception as e:
        return e


def check_results(id, string_from_user):
    try:
        ls_words_from_test = get_words_from_test(id)
        ls_from_user = string_from_user.split(" ")
        ls_words_from_test = [word["word"] for word in ls_words_from_test]

        if len(ls_from_user) < len(ls_words_from_test):
            delete_words_from_test(id)
            raise Exception("Not enough words")
        if len(ls_from_user) > len(ls_words_from_test):
            delete_words_from_test(id)
            raise Exception("To many words")
        wrong = []
        for i in range(len(ls_words_from_test)):
            p = ls_from_user[i]
            o = get_translate_word(ls_words_from_test[i])
            if ls_from_user[i] != get_translate_word(ls_words_from_test[i]):
                word_update_or_insert(id, ls_words_from_test[i])
                wrong.append(ls_words_from_test[i])
            else:
                update_quantity(id, ls_words_from_test[i])
        if not wrong:
            delete_words_from_test(id)
            return "You Are Very Smart! Everything is correct\n for more quiz click on /test"
        else:
            list_of_wrong_word = "Mistakes:\n"
            for i in wrong:
                list_of_wrong_word += i + ": " + get_translate_word(i) + "\n"
            delete_words_from_test(id)
            list_of_wrong_word = list_of_wrong_word + "for another quiz click on /test"
            return list_of_wrong_word
    except Exception as e:
        return Exception("error test_word")
