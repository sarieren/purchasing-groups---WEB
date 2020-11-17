from module_db_test import *
from translate_word import get_translate_word


def test_word(id, num=5):
    ls_of_test_word = find_words_for_test(id, num)
    print(ls_of_test_word)
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
            check_results(id, input)
    except Exception as e:
        return e


def check_results(id, string_from_user):
    try:
        ls_words_from_test = get_words_from_test(id)
        ls_from_user = string_from_user.split(" ")[::-1]
        print(ls_from_user)
        ls_words_from_test = [word["word"] for word in ls_words_from_test]
        print(ls_words_from_test)
        if len(ls_from_user) != len(ls_words_from_test):
            delete_words_from_test(id, ls_words_from_test)
            raise Exception("not equal length")
        wrong = []
        print("hy")
        for i in range(len(ls_words_from_test)):
            print(i)
            if ls_from_user[i] != get_translate_word(ls_words_from_test[i]):
                word_update_or_insert(id, ls_from_user[i])
                wrong.append(ls_words_from_test[i])
            else:
                update_quantity(id, ls_from_user[i])
        print("after first for")
        if not wrong:
            print("not wrong")
            delete_words_from_test(id, ls_words_from_test)
            return "you very smart! everything is correct\n for more quiz click on /test_word"
        else:
            list_of_wrong_word = "wrong words:\n"
            for i in wrong:
                list_of_wrong_word += i + ": " + get_translate_word(i) + "\n"
            delete_words_from_test(id, ls_words_from_test)
            return list_of_wrong_word + "\n for more quiz click on /test_word"
    except Exception as e:
        return Exception("error test_word")
