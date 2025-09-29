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


def add_birthday(user_id, name, date, user):
    data = read_users_data(bot_config['json_users'])
    user_id_str = str(user_id)

    if user_id_str not in data:
        data[user_id_str] = []

    data[user_id_str].append({
        'name': name,
        'date': date,
        'user': user,
    })

    write_users_data(data,bot_config['json_users'])

def add_engl( date,pay):
    data = read_users_data(bot_config['json_engl'])
    user_id = str(bot_config['admin'][0])

    if user_id not in data:
        data[user_id] = []

    data[user_id].append({
        'date': date,
        'pay': pay
    })

    write_users_data(data,bot_config['json_engl'])

def get_engl():
    data = read_users_data(bot_config['json_engl'])
    user_id = str(bot_config['admin'][0])
    return data.get(str(user_id), [])

def get_date(user_id):
    data = read_users_data(bot_config['json_users'])
    return data.get(str(user_id), [])


def update_engl(index, pay=None):
    data = read_users_data(bot_config['json_engl'])
    user_id = str(bot_config['admin'][0])

    if user_id in data and  index < len(data[user_id]) and index >= 0:
        if pay is not None:
            data[user_id][index]['pay'] = pay

        write_users_data(data, bot_config['json_engl'])

