from rest_framework.viewsets import ModelViewSet

from events_app.models.events import EventModel
from events_app.api.serializers.events import EventSerializer


class EventViewSet(ModelViewSet):
    queryset = EventModel.objects.all()
    serializer_class = EventSerializer
