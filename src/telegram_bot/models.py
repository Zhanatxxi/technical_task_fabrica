from django.db import models


class TelegramClient(models.Model):
    username = models.CharField(max_length=128, null=True, blank=True)
    first_name = models.CharField(max_length=128, null=True, blank=True)
    telegram_id = models.CharField(max_length=128, unique=True, db_index=True)
    token_api = models.CharField(max_length=255, unique=True, null=True, db_index=True)
