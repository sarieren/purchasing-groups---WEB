from module_test_word import test_word


def test_after_translate(id):
    try:
        return test_word(id, 2)
    except:
        raise Exception("error in test_after_translate")
