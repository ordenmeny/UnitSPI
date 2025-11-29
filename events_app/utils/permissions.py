from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed


class CustomIsAuthenticated(IsAuthenticated):
    def has_permission(self, request, view):
        user = request.user

        # Нет токена или аноним → кидаем исключение, которое твой handler поймает
        if not user or user.is_anonymous:
            raise AuthenticationFailed("Authentication credentials were not provided")

        return True
