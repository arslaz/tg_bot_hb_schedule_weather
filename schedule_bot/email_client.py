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

async def get_unseen_message():
    imap = await connect()
    if imap is None:
        return None

    imap.select_folder('INBOX')
    messages = imap.search(['UNSEEN', 'FROM', email_config['email_sender']])

    if not messages:
        imap.logout()
        return None

    last_uid = max(messages)
    raw_data = imap.fetch([last_uid], ['RFC822'])[last_uid][b'RFC822']
    msg = email.message_from_bytes(raw_data)

    body = None

    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == 'text/plain':
                payload = part.get_payload(decode=True)
                if isinstance(payload, bytes):
                    body = payload.decode('utf-8', errors='ignore')
                break
    else:
        payload = msg.get_payload(decode=True)
        if isinstance(payload, bytes):
            body = payload.decode('utf-8', errors='ignore')

    if body:
        imap.add_flags([last_uid], [b'\\Seen'])

    imap.logout()
    return body

