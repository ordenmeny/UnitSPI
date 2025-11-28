from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer, TokenRefreshSerializer)
from rest_framework_simplejwt.tokens import RefreshToken

from djangoProject import settings
from events_app.api.serializers.users import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class CustomTokenObtainView(APIView):
    serializer_class = TokenObtainPairSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        refresh_token = serializer.validated_data.pop("refresh")

        response = Response({"access": serializer.validated_data.get("access")})
        response.set_cookie(
            key="refresh_token",
            value=str(refresh_token),
            httponly=True,
            secure=settings.SECURE_COOKIE,
            samesite="Lax"
        )

        return response


class CustomTokenRefreshView(APIView):
    serializer_class = TokenRefreshSerializer

    def post(self, request):
        refresh_token = request.COOKIES.get("refresh_token")

        if refresh_token is None:
            raise InvalidToken("Refresh token not provided")

        try:
            refresh_token = RefreshToken(refresh_token)
            access_token = refresh_token.access_token
        except Exception as e:
            return Response(
                {"error": "Invalid refresh token"},
                status=status.HTTP_403_FORBIDDEN)

        response = Response({"access": str(access_token)}, status=status.HTTP_200_OK)

        return response
