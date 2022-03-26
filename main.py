import time
import requests
import datetime

api = '5247144957:AAFXYENO8wbqy3bNubz05xx38inPPQIBxBQ'
chat_id = '1741346039'


def start():
    send_message = rf'https://api.telegram.org/bot{api}/sendMessage?chat_id={chat_id}&text='
    shia_video = r'https://www.youtube.com/watch?v=ZXsQAXx_ao0'
    target_date = datetime.date(2022, 8, 31)
    current_date = datetime.date.today()
    messages_list = []

    while True:
        messages_list.append(
            requests.get(f'{send_message}*DAYS LEFT: {(target_date - current_date).days}*&parse_mode=MarkdownV2').json()['result']['message_id'])
        messages_list.append(
            requests.get(f'{send_message}[JUST DO IT!]\n{shia_video}').json()['result']['message_id'])
        time.sleep(3)
        delete_messages(messages_list)
        time.sleep(3)


def delete_messages(messages):
    for i in messages:
        requests.get(rf'https://api.telegram.org/bot{api}/deleteMessage?chat_id={chat_id}&message_id={i}')


start()
