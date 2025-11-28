from django.urls import path, include, re_path
from djangoProject.custom_router import EnhancedAPIRouter
from rest_framework.routers import APIRootView
from events_app.api.views.events import EventViewSet
from events_app.api.views.users import UserViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from events_app.api.views.users import CustomTokenObtainView, CustomTokenRefreshView


class HubAPIRootView(APIRootView):
    """Корневой view для апи."""

    __doc__ = 'Приложение хаб'
    name = 'hub'


router = EnhancedAPIRouter()
router.APIRootView = HubAPIRootView

router.register('events', EventViewSet, 'event')
router.register('users', UserViewSet, 'user')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/', CustomTokenObtainView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.jwt')),
]