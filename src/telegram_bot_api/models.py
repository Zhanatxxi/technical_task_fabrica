from django.db import models

from src.account.models import CustomUser


class TelegramMessage(models.Model):
    message = models.TextField(blank=True, null=True, verbose_name='Message from API')
    auth_id = models.ForeignKey(to=CustomUser,
                                on_delete=models.PROTECT,
                                related_name='telegram_messages')
    created_date = models.DateTimeField(auto_now=True)
