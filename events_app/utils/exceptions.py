from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework.exceptions import AuthenticationFailed


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    # Если токен просрочен или невалиден — меняем ответ
    if isinstance(exc, (InvalidToken, TokenError)):
        return Response(
            {"error": "access_not_valid", "step": "to_refresh"},
            status=status.HTTP_401_UNAUTHORIZED
        )

    if isinstance(exc, AuthenticationFailed):
        # access токен не предоставлен
        return Response(
            {"error": "access_missing", "step": "to_login"},
            status=status.HTTP_401_UNAUTHORIZED
        )

    return response
