from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

from config import settings
from src.telegram_bot.consumer import send_message
from src.telegram_bot.services import get_telegram_client_by_token
from src.telegram_bot_api.serializers import SendMessageSerializers, MessageSerializers


class SendMessageApi(APIView):

    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(tags=settings.TAGS["TELEGRAM"], request_body=SendMessageSerializers)
    def post(self, request):
        serializer = SendMessageSerializers(data=request.data, context={'auth_id': request.user})
        if serializer.is_valid(raise_exception=True):
            message = serializer.save()
            telegram_token = message.auth_id.profile.telegram_token
            telegram_client = get_telegram_client_by_token(telegram_token)
            if telegram_client.telegram_id:
                text = f"""{telegram_client.first_name or telegram_client.username}, я получил от тебя сообщение:\n{message.message} """
                send_message(message=text, telegram_id=telegram_client.telegram_id)
                return Response('message saved and send telegram', status=status.HTTP_201_CREATED)
            return Response('message saved but not send telegram', status=status.HTTP_201_CREATED)

    @swagger_auto_schema(tags=settings.TAGS["TELEGRAM"])
    def get(self, request):
        user = request.user
        messages = user.telegram_messages.all()
        serializer = MessageSerializers(instance=messages, many=True)
        return Response(data=serializer.data)
