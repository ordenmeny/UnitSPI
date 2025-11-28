from django.urls import path, include
from djangoProject.custom_router import EnhancedAPIRouter
from rest_framework.routers import APIRootView
from events.views import EventViewSet


class HubAPIRootView(APIRootView):
    """Корневой view для апи."""

    __doc__ = 'Приложение хаб'
    name = 'hub'


router = EnhancedAPIRouter()
router.APIRootView = HubAPIRootView

router.register('', EventViewSet, 'event')

urlpatterns = [
    path('', include(router.urls)),
]
