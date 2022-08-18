import json
import requests

class TelegramBot:
    def __init__(self, pipeline):
        self.token = "5403008172:AAGt3ZsSDSN_jdmKlID8Ml3J-gL8q-vQCsA"
        self.url = f"https://api.telegram.org/bot{self.token}"
        self.pipeline = pipeline

    def get_updates(self, offset=None):
        url = self.url + "/getUpdates?timeout=100"
        if offset:
            url = url + f"&offset={offset + 1}"
        url_info = requests.get(url)
        return json.loads(url_info.content)

    def sent_msg(self, msg, chat_id):
        url = self.url + f'/sendMessage?chat_id={chat_id}&text={msg}'
        if msg is not None:
            requests.get(url)

    def generate_response(self, user_text):
        pred = self.pipeline.predict([user_text])[0]

        if pred == "religion_bullying":
            pred = "It's none of your business"
        elif pred == "age_bullying":
            pred = "But I'm smart beyond my years"
        elif pred == "gender_bullying":
            pred = "It doesn't matter what your gender is, you should remain human"
        else:
            pred ="You are so cute"
        return pred