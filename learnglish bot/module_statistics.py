from module_db_test import get_words_quantity_sorted_descending_order

def get_static(id):
    lst_words = get_words_quantity_sorted_descending_order(id)
    lst_word = [word["word"] for word in lst_words]
    lst_quantity = [quantity["quantity"] for quantity in lst_words]
    index = 0
    statistics = "<b>"+"Most Common Words Are:"+"</b>"+"\n\n"

    while index < len(lst_word):
        statistics = statistics + lst_word[index] + "\t - \t" + str(lst_quantity[index])+"\n"
        index += 1
    return statistics
