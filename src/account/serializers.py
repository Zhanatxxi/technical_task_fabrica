from django.contrib.auth import authenticate, get_user_model
from django.core.mail import send_mail
from rest_framework import serializers

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, required=True)
    password_confirm = serializers.CharField(min_length=6, required=True)

    class Meta:
        model = User
        fields = (
            'email',
            'password',
            'password_confirm',
            'first_name'
        )

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('this user is login')
        return email

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.pop('password_confirm')
        if password != password_confirm:
            raise serializers.ValidationError('passwords not !=')
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerialiser(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(username=email, password=password, request=self.context.get('request'))
            if not user:
                raise serializers.ValidationError('wrong enter email and password')
        else:
            raise serializers.ValidationError('Email and Password they required')
        attrs['user'] = user
        return attrs