import os
from dotenv import load_dotenv

load_dotenv()

email_config = {
    'server': os.getenv('EMAIL_SERVER', 'imap.gmail.com'),
    'email': os.getenv('EMAIL_ADDRESS'),
    'password': os.getenv('EMAIL_PASSWORD'),
    'email_sender': os.getenv('EMAIL_SENDER')
}

bot_config = {
    'bot_token': os.getenv('BOT_TOKEN'),
    'admin': os.getenv('ADMIN_IDS', '').split(','),
    'json_users': os.getenv('JSON_USERS', 'users.json'),
    'json_engl': os.getenv('JSON_ENGL', 'engl.json')
}
