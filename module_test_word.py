from module_db_test import *
from translate_word import get_translate_word


def test_word(id, num = 5):
    try:
        ls_of_test_word = find_words_for_test(id, num)
        insert_words_test(id, ls_of_test_word)
        string_to_return = '<b>' + 'Words to translate: \n\n' + '</b>'
        for word in ls_of_test_word:
            string_to_return += word
            string_to_return += '\n'
        string_to_return += '<b>' + '\nAnswer by order with comma between the words'+'</b>'
        return string_to_return
    except Exception as e:
        return e



def menu_test_word(id, input):
    try:
        if input == "/test":
            return test_word(id)
        else:
            return check_results(id, input)
    except Exception as e:
        raise Exception(e)


def check_results(id, string_from_user):
    try:
        ls_words_from_test = get_words_from_test(id)
        if("," in string_from_user):
            ls_from_user = string_from_user.split(",")
            ls_from_user = [word.strip() for word in ls_from_user]
        else:
            ls_from_user = string_from_user
        ls_words_from_test = [word["word"] for word in ls_words_from_test]

        if len(ls_from_user) < len(ls_words_from_test):
            delete_words_from_test(id)
            raise Exception("Not enough words")
        if len(ls_from_user) > len(ls_words_from_test):
            delete_words_from_test(id)
            raise Exception("Too many words")
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
            return "You Are Very Smart! Everything is correct🥳\n"
        else:
            list_of_wrong_word = "Your Mistakes Are 😢:\n"
            for i in wrong:
                list_of_wrong_word += i + ": " + get_translate_word(i) + "\n"
            delete_words_from_test(id)
            list_of_wrong_word = list_of_wrong_word
            return list_of_wrong_word
    except Exception as e:
        delete_words_from_test(id)
        return Exception("error test_word")
