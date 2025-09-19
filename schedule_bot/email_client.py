import imapclient
import email
from config import *

async def connect():
    imap = imapclient.IMAPClient(email_config['server'], ssl=True)
    try:
        imap.login(email_config['email'], email_config['password'])
        return imap
    except Exception as e:
        print(f"Ошибка подключения: {e}")
        return None

async def search_message(imap):
    imap.select_folder('INBOX')
    message = imap.search(['FROM', email_config['email_sender']])
    body = ""
    if message:
        raw_data = imap.fetch([max(message)], ['RFC822'])[max(message)][b'RFC822']
        message = email.message_from_bytes(raw_data)

        body = message.get_payload(decode=True)
        if isinstance(body, bytes):
            body = body.decode('utf-8', errors='ignore')
        return body
    else:
        return None

