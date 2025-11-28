from django.contrib import admin
from django.urls import path, include
from events.urls import router as event_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/events/', include(event_router.urls)),
]

