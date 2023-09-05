from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from config.logger import get_logger
from config import settings
from src.account.serializers import RegisterSerializer, LoginSerialiser


logger = get_logger(__name__)


class RegistrationView(APIView):

    @swagger_auto_schema(
        request_body=RegisterSerializer,
        tags=settings.TAGS["AUTH"]
    )
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('your account successfully registration', status=status.HTTP_201_CREATED)


class LoginView(ObtainAuthToken):
    serializer_class = LoginSerialiser

    @swagger_auto_schema(tags=settings.TAGS["AUTH"])
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(tags=settings.TAGS["AUTH"])
    def post(self, request):
        Token.objects.filter(user=request.user).delete()
        return Response('you successfully logout!')


class GetTokenAccount(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=settings.TAGS["AUTH"],
        operation_description="generate new telegram token"
    )
    def put(self, request):
        user = request.user
        user.profile.generate_telegram_token()
        user.profile.save()
        return Response('generate new telegram token')

    @swagger_auto_schema(
        tags=settings.TAGS["AUTH"],
        operation_description="get telegram token"
    )
    def get(self, request):
        return Response(request.user.profile.telegram_token)
