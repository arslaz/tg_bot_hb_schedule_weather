import json
from config import *

def read_users_data(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def write_users_data(data,file):
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def add_subscriber(chat_id):
    data = read_users_data('subscribers.json')
    chat_id_str = str(chat_id)
    if chat_id_str not in data:
        data[chat_id_str] = True
        write_users_data(data, 'subscribers.json')
        return True  # новый подписчик
    return False  # уже есть

def get_subscribers():
    data = read_users_data('subscribers.json')
    return [int(k) for k in data.keys()]

