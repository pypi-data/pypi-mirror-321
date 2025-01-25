import requests

from django.conf import settings


TELEGRAM_BOT_TOKEN = getattr(settings, "ERRFORMER_TELEGRAM_BOT_TOKEN")
ADMIN_CHAT_ID = getattr(settings, "ERRFORMER_ADMIN_CHAT_ID")


def send_telegram_message_to_admin(message):
    """
    Send message to telegram chat of admin
    """
    if not TELEGRAM_BOT_TOKEN or not ADMIN_CHAT_ID:
        print("Telegram bot token or admin chat id is not set")
        return
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage?parse_mode=HTML"
    payload = {
        'chat_id': ADMIN_CHAT_ID,
        'text': message,
    }
    response = requests.post(url, json=payload)
    return response.json()
