from rest_framework.viewsets import ModelViewSet

from events.models import EventModel
from events.serializers import EventSerializer


class EventViewSet(ModelViewSet):
    queryset = EventModel.objects.all()
    serializer_class = EventSerializer