from module_db_state import get_state, insert_or_update_state
from module_test_word import menu_test_word, check_results
from translate_word import menu_translate_word
from test_after_translate import test_after_translate
from module_study_word import menu_study_word

def get_main_menu():
    try:
        main_menu = "Please click on the action you want to perform:" \
                    "\n\n /study_word \n\n /test \n\n /translate_word"
        return main_menu
    except:
        return "error in main_menu"



def choose_action(id, input):
    try:
        if(input == "/go_back" and get_state(id) == "menu_translate_word"):
            insert_or_update_state(id, "test_after_translate")
            return test_after_translate(id)

        elif (input == "/start" or input == "/go_back"):
            insert_or_update_state(id, "main_menu")
            return get_main_menu()

        elif input == "/translate_word" and get_state(id) == "main_menu":
            insert_or_update_state(id, "menu_translate_word")
            return menu_translate_word(id, input)
        elif input == "/study_word" and get_state(id) == "main_menu":
            insert_or_update_state(id, "menu_study_word")
            return menu_study_word(id, input)
        elif input == "/test" and get_state(id) == "main_menu":
            insert_or_update_state(id, "menu_test_word")
            return menu_test_word(id, input)


        elif (input == "/study_word" or input == "/next") and get_state(id) == "menu_study_word":
            return menu_study_word(id, input)
        elif get_state(id) == "menu_translate_word":
            return menu_translate_word(id, input)
        elif get_state(id) == "menu_test_word":
            return menu_test_word(id, input)
        elif get_state(id) == "test_after_translate":
            return check_results(id, input)
        else:
            return "invalid value"

    except Exception as e:
        return e

