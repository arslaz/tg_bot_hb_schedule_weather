import json
from config import *

def read_users_data():
    try:
        with open(bot_config['json_users'], 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def write_users_data(data):
    with open(bot_config['json_users'], 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def add_birthday(user_id, name, date, user):
    data = read_users_data()
    user_id_str = str(user_id)

    if user_id_str not in data:
        data[user_id_str] = []

    data[user_id_str].append({
        'name': name,
        'date': date,
        'user': user,
    })

    write_users_data(data)


def get_date(user_id):
    data = read_users_data()
    return data.get(str(user_id), [])