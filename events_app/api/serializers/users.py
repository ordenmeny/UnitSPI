from typing import Any

from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'chat_id', 'tg_link', 'first_name', 'last_name')
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        validated_data["username"] = validated_data["email"]
        password = validated_data.pop("password")

        user = super().create(validated_data)
        user.set_password(password)
        user.save()

        return user

# class CustomObtainPairSerializer(TokenObtainPairSerializer):
#     def validate(self, attrs: dict[str, Any]) -> dict[str, str]:
#         data = super().validate(attrs)
#
#         refresh = self.get_token(self.user)
#
#         data["refresh"] = str(refresh)
#         data["access"] = str(refresh.access_token)
#
#         return data

# class CustomTokenRefreshSerializer(TokenRefreshSerializer):
#     pass
