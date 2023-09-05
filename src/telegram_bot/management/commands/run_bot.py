from django.core.management.base import BaseCommand

from src.telegram_bot.main import run_main_bot


class Command(BaseCommand):
    help = "runner telegram bot"

    def handle(self, *args, **options):
        run_main_bot()
