from django.urls import path

from src.telegram_bot_api.views import SendMessageApi


urlpatterns = [
    path('message/', SendMessageApi.as_view())
]