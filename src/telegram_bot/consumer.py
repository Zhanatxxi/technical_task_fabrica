import telegram
import requests

from config import settings


def send_message(telegram_id: str | int, message: str):
    SEND_URL = f'https://api.telegram.org/bot{settings.TELEGRAM_TOKEN}/sendMessage'

    requests.post(SEND_URL, json={'chat_id': telegram_id, 'text': message})
