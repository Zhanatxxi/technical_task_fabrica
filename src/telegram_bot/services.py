from django.db import IntegrityError

from config.logger import get_logger
from src.telegram_bot.models import TelegramClient

logger = get_logger(__name__)


async def create_telegram_client(
    *,
    username: str,
    first_name: str,
    telegram_id: str | int,
    token_api: str
) -> TelegramClient:
    try:
        client = await TelegramClient.objects.acreate(
            username=username,
            first_name=first_name,
            telegram_id=telegram_id,
            token_api=token_api
        )
    except IntegrityError as e:
        logger.error(e)
        client = await TelegramClient.objects.aget(telegram_id=telegram_id)
        client.token_api = token_api
        await client.asave()
    else:
        return client


def get_telegram_client_by_token(token) -> TelegramClient | None:
    try:
        return TelegramClient.objects.get(token_api=token)
    except TelegramClient.DoesNotExist as e:
        logger.error(e)
        return None
