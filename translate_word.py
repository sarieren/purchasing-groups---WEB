from translate import Translator
from module_db_state import insert_or_update_state
from module_db_words import word_update_or_insert


def menu_translate_word (id, input):
    try:
        if(input == "/translate_word" or input == "/next"):
            return "Please enter one word for translation"
        elif(input == "/go_back"):
            return  insert_or_update_state(id,"main_menu")
        else:
            return translate_word_and_update_db(id, input)
    except:
         return Exception("study words error")


def get_translate_word(word_to_translate):
    try:
        translator = Translator(to_lang="iw")
        my_translation = translator.translate(word_to_translate)
        return my_translation

    except:
        return Exception("error in word")


def translate_word_and_update_db(id, word_to_translate):
    try:
        if(" " in word_to_translate):
            return "you can translate only one word"
        else:
            translate = get_translate_word(word_to_translate)
            word_update_or_insert(id, word_to_translate)

            menu = "\n\n If you want to translate another word please send another word. \n" \
                   "To return to the main menu click /go_back"

            result = "The translate of " + word_to_translate + "\nis: " + translate + menu
            return result

    except Exception as e:
        return e

