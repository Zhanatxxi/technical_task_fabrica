from rest_framework import serializers

from src.telegram_bot_api.models import TelegramMessage


class SendMessageSerializers(serializers.Serializer):
    message = serializers.CharField()

    def create(self, validated_data):
        auth_id = self.context.get('auth_id')
        return TelegramMessage.objects.create(**validated_data, auth_id=auth_id)


class MessageSerializers(serializers.ModelSerializer):

    class Meta:
        model = TelegramMessage
        fields = ('message', 'created_date')
        ordering = ('-created_date', )
