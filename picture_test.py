import requests

from module_test_word import *
from module_db_images import get_word_image



def get_url(id):
    try:
        common_word = get_word_image()
        piece_url = 'https://pixabay.com/api/?key=19156012-fe856b2884e74c41ff3f38122&q={}&image_type=photo'.format(common_word)
        respone = requests.get(url=piece_url)
        result = respone.json()
        if(result):
            result_url = get_url_and_enter_to_db(id, result, common_word)
        else:
            raise Exception("error in link")

        menu = "Please enter the translation of the image"
        return menu + '\n\n' + result_url
    except Exception as e:
        raise Exception(e)


def enter_tag_to_db(id, tags, common_word):
    try:
        if ("," in tags):
            list_of_tags = tags.split(",")
            list_of_tags = [tag.strip() for tag in list_of_tags]
        else:
            list_of_tags = [tags]
        if common_word in list_of_tags:
            insert_words_test(id, list_of_tags)
        else:
            list_of_tags.append(common_word)
            insert_words_test(id, list_of_tags)
    except Exception as e:
        raise Exception(e)



def get_url_and_enter_to_db(id, all_links, common_word):
    try:
        for information in all_links["hits"]:
            if common_word in information["pageURL"]:
                enter_tag_to_db(id, information["tags"], common_word)
                return information["webformatURL"]

        enter_tag_to_db(id, all_links["hits"][0]["tags"], common_word)
        return all_links["hits"][0]["webformatURL"]
    except Exception as e:
        raise Exception(e)


def check_result_picture(id, picture_translate):
    try:
        ls_words_from_test = get_words_from_test(id)
        ls_words_from_test = [word["word"] for word in ls_words_from_test]


        if(picture_translate in ls_words_from_test):
            answer = "You're right!!\n\n"
        else:
            answer = "the answer can be:\n"
            for word in ls_words_from_test:
                answer = answer + word + '\n'
            answer += '\n'

        delete_words_from_test(id)
        menu = "for another quiz with picture click on /picture_test\n for return click /go_back"
        return answer + menu
    except Exception as e:
        raise Exception(e)
