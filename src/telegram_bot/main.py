import asyncio

from telegram import Update
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler

from config import settings
from config.logger import get_logger
from src.telegram_bot.services import create_telegram_client

logger = get_logger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await create_telegram_client(
        username=update.effective_chat.username,
        first_name=update.effective_chat.first_name,
        telegram_id=update.effective_chat.id,
        token_api=update.message.text
    )
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Set new Token")


def run_main_bot():
    application = ApplicationBuilder().token(settings.TELEGRAM_TOKEN).build()

    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)

    application.add_handler(start_handler)
    application.add_handler(echo_handler)

    application.run_polling()


if __name__ == '__main__':
    run_main_bot()

