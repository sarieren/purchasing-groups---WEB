import requests


def get_picture(item_name):
    try:
        
        piece_url = 'https://pixabay.com/api/?key=19156012-fe856b2884e74c41ff3f38122&q={}&image_type=photo'.format(item_name)
        respone = requests.get(url=piece_url)
        result = respone.json()
        # if(result):
        #     result_url = get_url_and_enter_to_db(result, item_name)
        # else:
        #     raise Exception("error in link")

        return result["hits"]

    except Exception as e:
        raise Exception(e)



def get_url_and_enter_to_db(all_links, item_name):
    try:
        for information in all_links["hits"]:
            if item_name in information["pageURL"]:
                return information["webformatURL"]

        return all_links["hits"][0]["webformatURL"]
    except Exception as e:
        raise Exception(e)


