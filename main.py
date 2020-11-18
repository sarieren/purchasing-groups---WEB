from flask import Flask, Response, request
from module_choose_action import choose_action
import requests


TOKEN = '1267251022:AAGxFzIuefMui68W-YF-gHBg2nv08CJ1Vd8'
TELEGRAM_INIT_WEBHOOK_URL = 'https://api.telegram.org/bot{}/setWebhook?url=https://34585cf2a9bb.ngrok.io/message'.format(TOKEN)

requests.get(TELEGRAM_INIT_WEBHOOK_URL)




app = Flask(__name__)


@app.route('/message', methods=["POST"])
def handle_message():
    input = request.get_json()['message']['text']
    chat_id = request.get_json()['message']['chat']['id']
    result = choose_action(chat_id, input)

    res = requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"
                       .format(TOKEN, chat_id, result))
    return Response("success")




app.run(port=5002)