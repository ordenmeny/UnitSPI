from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'chat_id', 'tg_link', 'first_name', 'last_name', 'password')
        extra_kwargs = {"password": {"write_only": True}}

    @staticmethod
    def validate_password(password):
        try:
            validate_password(password)
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)
        return password

    def create(self, validated_data):
        validated_data["username"] = validated_data["email"]
        password = validated_data.pop("password")

        user = super().create(validated_data)
        user.set_password(password)
        user.save()

        return user



