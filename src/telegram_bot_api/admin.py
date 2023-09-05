from django.contrib import admin

from src.telegram_bot_api.models import TelegramMessage

admin.site.register(TelegramMessage)